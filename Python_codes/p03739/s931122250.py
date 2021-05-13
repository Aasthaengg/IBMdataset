N = int(input())
A = list(map(int,input().split()))
ans = 10**15

for s in [1,-1]:
  cos = 0
  tot = 0
  
  for a in A:
    tot+=a
    if s*tot<=0:
      cos+=abs(tot-s)
      tot=s
    s*=-1
  
  ans=min(ans,cos)

print(ans)
