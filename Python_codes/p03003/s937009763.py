N,M=map(int,input().split())
s=list(map(int,input().split()))
t=list(map(int,input().split()))
mod=10**9+7
sm=[[ 0 for i in range(M)] for j in range(N)]
s1=0
s2=0
if N>M:
  for i in range(N):
    if t[0]==s[i]:
      a=1
    else:
      a=0
    s1=s1+a
    sm[i][0]=s1
    if i<M:
      if s[0]==t[i]:
        a=1
      else:
        a=0
      s2=s2+a
      sm[0][i]=s2
else:
  for i in range(M):
    if s[0]==t[i]:
      a=1
    else:
      a=0
    s2=s2+a
    sm[0][i]=s2
    if i<N:
      if t[0]==s[i]:
        a=1
      else:
        a=0
      s1=s1+a
      sm[i][0]=s1
for i in range(1,N):
  for j in range(1,M):
    if s[i] != t[j]:
      sm[i][j]=(sm[i-1][j]+sm[i][j-1]-sm[i-1][j-1])%mod
    else:
      sm[i][j]=(sm[i-1][j]+sm[i][j-1]-sm[i-1][j-1]+sm[i-1][j-1]+1)%mod
ans=(sm[N-1][M-1]+1)%mod
print(ans)