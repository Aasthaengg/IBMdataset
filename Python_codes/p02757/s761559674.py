N,P=[int(s) for s in input().split()]
S=list(input())
if P!=2 and P!=5:
  ls=[0 for _ in range(N)]
  mod=[0 for _ in range(P)]
  d=10
  ls[0]=int(S[-1])%P
  mod[ls[0]]+=1
  for i in range(1,N):
    ls[i]=(ls[i-1]+d*int(S[-1-i]))%P
    d=(d*10)%P
    mod[ls[i]]+=1
  #print(ls)
  #print(mod)  
  ans=mod[0]
  for i in range(N):
    m=ls[i]
    mod[ls[i]]-=1
    ans+=mod[ls[i]]
else:
  ans=0
  for i in range(N):
    if int(S[i])%P==0:
      ans+=i+1
print(ans)
   
