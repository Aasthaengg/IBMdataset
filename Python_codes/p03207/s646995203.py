N = int(input())
ans = 0
m = 0
for i in range(N):
  k = int(input())
  ans += k
  m = max(m, k)
print( ans - m//2)