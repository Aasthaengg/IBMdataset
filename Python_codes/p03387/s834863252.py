A,B,C=map(int,input().split())
L=[A,B,C]
L=sorted(L)
ans=0
ans+=L[2]-L[1]
L[0]+=L[2]-L[1]
ans+=(L[2]-L[0])//2
L[0]+=((L[2]-L[0])//2)*2
if L[0]!=L[2]:
  ans+=2
print(ans)