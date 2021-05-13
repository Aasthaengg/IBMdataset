k,s=map(int,input().split())
upper  = min(k,s)+1
lower = max(0,s-2*k)
ans = 0
for i in range(lower,upper):
  for j in range(lower,upper):
    if 0 <= s-(i+j) <= k:
      ans += 1
print(ans)