n,t = map(int,input().split())
ans = 10 **5
for i in range(n):
  a,b = map(int,input().split())
  if t >= b:
    ans = min(a,ans)
print(ans if ans < 10000 else "TLE")