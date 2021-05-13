N,M=map(int,input().split())
dp=[0]*(2*(10**5)+1)
bp=[0]*(2*(10**5)+1)
for _ in range(M):
  a,b=map(int,input().split())
  if a==1:
    if bp[b]==1:
      print('POSSIBLE')
      exit()
    dp[b]+=1
  if b==N:
    if dp[a]==1:
      print('POSSIBLE')
      exit()
    bp[a]+=1
print('IMPOSSIBLE')