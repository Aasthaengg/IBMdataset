n=int(input())
S=[input() for _ in range(n)]

ans,acnt,bcnt,abcnt=0,0,0,0
for s in S:
  ans+=s.count('AB')
  if s[-1]=='A' and s[0]=='B': abcnt+=1
  elif s[-1]=='A': acnt+=1
  elif s[0]=='B': bcnt+=1
if abcnt:
  ans+=abcnt-1
  if acnt:
    ans+=1
    acnt-=1
  if bcnt:
    ans+=1
    bcnt-=1
ans+=min(acnt,bcnt)
print(ans)