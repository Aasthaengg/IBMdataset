N, K = map(int, input().split())

p = list(map(int, input().split()))
c = list(map(int, input().split()))

for i in range(len(p)):
    p[i] -= 1

ans = float("-inf")

for i in range(N):
    #iはスタートポジション
    pos = i
    #移動先のマスにかかれたポイント
    point = []
    total = 0
    while True:
        pos = p[pos]
        point.append(c[pos])
        # totalは周期の和がマイナスかプラスかで後々場合分けするために使う。(周期が負だったら一巡目で終わらせたい。周期が正だったらできる限り後の方で終わらせたい)
        total += c[pos]
        #スタートポジションに戻ってきた==サイクルを検知した
        if pos == i: break
    l = len(point)

    t = 0
    #total<0のときはif total>0以外の処理でまきとれる
    for i in range(l):
        t += point[i]
        #Kがi+1より小さい時のハンドリング
        if i+1 > K: break
        now = t
        if total > 0:
            #K-i-1の-1はポイントの一個目を獲得する時に1個動くので-1。二こ目のポイントを取る時はi=1で、K-2になり計算が合う。それをlでわり周期が何個回れるかを計算する
            #nowはtotalのセットが何個かあって、その先にpoint[i]がくっつくイメージ。[a,b,c] + [a,b,c] + [a,b,c] + ([a] or [a+b] + [a+b+c]) 
            #最初now += total * (K-i-1)//lとしていてWAしていたので書き方注意。これだとtotalと(K-i-1)をかけたものをlでわる、となってしまう。
            cnt = (K-i-1) // l
            now += total * cnt 
        ans = max(ans, now)
print(ans)