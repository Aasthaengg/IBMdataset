N = int(input())
ans = 0
d = 1
while d * d < N:
  if N % d == 0:
    m = (N // d) - 1
    if d < m:
    	ans += m
  d += 1
print(ans)
