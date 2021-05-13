N, D = map(int, input().split())
X_Y = []
for i in range(N):
    X_Y.append(list(map(int, input().split())))
    
ans = 0
for n in range(N):
  x, y = X_Y[n]
  # ルートを計算すると計算誤差が生じるので、距離の2乗を比較する
  if(x**2 + y**2 <= D*D): ans += 1

print(ans)