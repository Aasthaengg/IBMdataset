n,k = map(int,input().split())
v = list(map(int,input().split()))
r = min(n,k)
ans = -10**10
for i in range(0,r+1):
  for a in range(i+1):
    b = i - a
    val = sorted(v[:a]+v[(n-b):])
    s = sum(val)
    for j in range(min(k-i,len(val))):
      if val[j] < 0:
        s -= val[j]
      else:
        break
    ans = max(ans,s)
print(ans)