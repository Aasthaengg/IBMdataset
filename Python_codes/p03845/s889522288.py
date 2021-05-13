n = int(input())
t = list(map(int, input().split()))
m = int(input())
p = [[]] * m
x = [[]] * m
ans = 0
for i in range(n):
  ans += t[i]
for i in range(m):
  p[i], x[i] = map(int, input().split())
  print(ans - t[p[i]-1] + x[i])