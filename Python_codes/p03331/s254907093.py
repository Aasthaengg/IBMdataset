def solve(x):
  n = len(str(x))
  res = 0
  for i in str(x):
    res += int(i)
  return res

n=int(input())
ans = 10**20
for a in range(1,n):
  ans = min(ans,solve(a)+solve(n-a))
print(ans)