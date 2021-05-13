#入力
r, D, x0 = list(map(int,input().split()))
#数列xのリストを作っておく
x = [None for _ in range(10)]
#数列xの初項をリスト中に加えておく
x.insert(0,x0)
#与えられた数列に従い代入する, 結果
for i in range(1,11):
  x[i] = r * x[i-1] - D
  print(x[i])
