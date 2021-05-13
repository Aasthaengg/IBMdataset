import bisect
n = int(input())
l = sorted(list(map(int,input().split())))
ans = 0          
for ai in range(n):
  for bi in range(ai+1,n):
    ci = bisect.bisect_left(l,l[ai]+l[bi])
    if ci>bi:
      ans += ci-bi-1
print(ans)