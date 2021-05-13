n, k, s = list(map(int, input().split()))
ans = s + 1
if s == 10e8:
  ans = 1
for i in range(k):
  print(s, " ", end="")
for i in range(n-k):
  print(ans, " ", end="")