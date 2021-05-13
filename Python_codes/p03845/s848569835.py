n = int(input())
t = list(map(int, input().split()))
m = int(input())

for _ in range(m):
  ans = sum(t)
  p,x = map(int, input().split())
  ans -= t[p-1]
  ans += x
  print(ans)