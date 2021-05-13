#Satoooh
'''
左からL個、右からR個、取り出す。
取り出す回数は操作回数上限のK回なので、最大K個取り出せる。
操作はK回まで行えるので、操作回数がKより小さくてもOK。
求めるのは、価値の最大値なので、マイナスの宝石は、筒に戻す。
筒に戻せる上限は、下記１と２の小さい値min
１．操作回数制限：K-L-R、操作回数の上限から、LとRを取り出した回数を引く
２．宝石個数制限：手持ちは、L+R個なので、これ以上は戻せない
'''
N, K = map(int, input().split())
*V, = map(int, input().split())#タプルとして入力、仮に1個でもOK
ans = 0#格納されている宝石が負ばかりなら、何もしない

for l in range(K + 1):#左から最大K個取り出す
	for r in range(K - l + 1):
    #右から取り出すのはK-L個、左からL個取り出しているので
		inHand = []#手持ちを格納する配列
		if l + r > N:  # Nを超えてしまうありえない場合を処理
			break#ありえないケースはブレイク
		# inHandに左からl個、右からr個の要素を追加
		inHand = V[: l]
		inHand.extend(V[N - r:])
		tmp = sum(inHand)  
        # 現時点でのinHandの和をtmpとして負の要素をtmpから引いていく
		# inHand中の負の要素を消せるだけ消す
		inHand.sort()
		for i in range(min(K - l - r, l + r)):
			if inHand[i] >= 0:#負の要素だけ消す
				break
			tmp -= inHand[i]#負の要素は手持ちしないことにする
		ans = max(ans, tmp)#求めるのは手持ちの価値の最大値

print(ans)