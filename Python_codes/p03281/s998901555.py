def solve(n):
  cnt = 0
  for i in range(1,n+1):
    if n%i == 0: cnt += 1
  if cnt == 8: return True
  else: return False

n = int(input())
ans = 0
for i in range(1, n+1, 2):
  if solve(i): ans += 1
print(ans)