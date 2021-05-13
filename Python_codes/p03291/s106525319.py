s=input()
n=len(s)
q=s.count("?")
mod=10**9+7
def f(x,y,z):
  DP=[[0]*3 for _ in range(n+1)]
  for i in range(n):
    if s[i]==x:
      DP[i+1][0]=DP[i][0]+1
    else:
      DP[i+1][0]=DP[i][0]
    if s[i]==y:
      DP[i+1][1]=DP[i][1]+DP[i][0]
    else:
      DP[i+1][1]=DP[i][1]
    if s[i]==z:
      DP[i+1][2]=DP[i][2]+DP[i][1]
    else:
      DP[i+1][2]=DP[i][2]
  return DP[n][2]
ans=0
ans+=f("A","B","C")*3**q%mod
if q>=1:
  ans+=f("?","B","C")*3**(q-1)%mod
  ans+=f("A","?","C")*3**(q-1)%mod
  ans+=f("A","B","?")*3**(q-1)%mod
if q>=2:
  ans+=f("A","?","?")*3**(q-2)%mod
  ans+=f("?","B","?")*3**(q-2)%mod
  ans+=f("?","?","C")*3**(q-2)%mod
if q>=3:
  ans+=f("?","?","?")*3**(q-3)%mod
print(ans%mod)
