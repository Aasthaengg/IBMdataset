N,K=map(int,input().split())
A=list(map(int,input().split()))
One=[0]*40
OneK=format(K, '040b')
flg=True
for i in range(40):
  for j in range(N):
    if A[j]==0:
      continue
    flg=False
    One[39-i]+=A[j]&1
    A[j]=A[j]>>1
  if flg:
    break
  flg=True
ans=0
i=0
while i<40:
  if OneK[i]=='1':
    break
  ans+=pow(2,39-i)*One[i]
  i+=1
flg=False
while i<40:
  if One[i]>=N/2:
    ans+=pow(2,39-i)*One[i]
    if OneK[i]=='1':
      flg=True
  else:
    if flg or OneK[i]=='1':
      ans+=pow(2,39-i)*(N-One[i])
    else:
      ans+=pow(2,39-i)*One[i]
  i+=1
print(ans)