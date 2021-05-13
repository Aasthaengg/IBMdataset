import sys
input = sys.stdin.readline
N, X = map(int, input().split())
a = list(map(int, input().split()))
res = 0
for i in range(N - 1):
  if a[i] + a[i + 1] > X:
    if a[i] <= X:
      res += a[i] + a[i + 1] - X
      a[i + 1] -= a[i] + a[i + 1] - X
    else:
      res += a[i] + a[i + 1] - X
      a[i + 1] = 0
print(res)