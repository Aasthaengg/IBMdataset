#入力
n,m = map(int,input().split())
a_list = [input() for nesya in range(n)]
b = [input() for motsu in range(m)]

#二重ループによりN*NからM*Mの正方形を取り出す(j行目i列目)
for i in range(n-m+1):
  for j in range(n-m+1):
    #j~j+m-1行目のi~i+m-1列目をリスト型にする
    s = [(a_list[k])[i:i+m] for k in range(j,j+m)]
    #テンプレート(問題文)と一致しているか
    if b == s:
      #一致していたら終わる
      break
    #違ったら続ける
  #一致していた時、外側のリストについても終了する
  if b == s:
    break    

#判定
if b == s:
  #含んでいた
  print('Yes')
else:
  #含んでいなかった
  print('No')