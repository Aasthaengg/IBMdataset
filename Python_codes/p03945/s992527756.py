S=list(input())
ans=0
now=S[0]
for s in S:
  if s==now:
    continue
  ans+=1
  now=s
print(ans)