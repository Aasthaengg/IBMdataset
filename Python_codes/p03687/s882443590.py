S = input()

ans = 100
for s in S:
  n=list(map(len,S.split(s)))
  ans=min(ans,max(n))

print(ans)