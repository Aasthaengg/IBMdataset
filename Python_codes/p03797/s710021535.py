S,C=map(int,input().split())
ans=0
#1
ans+=min(S,C//2)
S,C=S-ans,C-ans*2
if C>1:
  ans+=C//4
print(ans)