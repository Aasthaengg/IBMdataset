N,P=map(int,input().split())
S=input()
sn=int(S)

if P==2:
  ans=0
  for i in range(1,N+1):
    if int(S[-i])%2==0:
      ans+=N-i+1
  print(ans)
  exit()

if P==5:
  ans=0
  for i in range(1,N+1):
    if int(S[-i])%5==0:
      ans+=N-i+1
  print(ans)
  exit()

amari=[0]*P
amari[0]=1

mod=0
for i in range(1,N+1):
  mod=(mod+int(S[-i])*pow(10,i-1,P))%P
  amari[mod]+=1
ans=0
for tmp in amari:
  ans+=tmp*(tmp-1)//2
  
print(ans)