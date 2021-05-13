N = int(input())
takahashi = 1
aoki = 1
for _ in range(N):
  t, a = map(int, input().split())
  X = -(-(takahashi + t-1))//t # 切り上げ
  Y = -(-(aoki + a-1))//a      # 切り上げ
  n = max(X, Y)
  takahashi = t*n
  aoki = a*n
  
print(int(takahashi+aoki))