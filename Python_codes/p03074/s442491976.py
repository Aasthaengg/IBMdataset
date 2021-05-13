N,K=map(int,input().split())
S=list(input())
T=[int(a) for a in S]
U=[]

if N==1:
  U=[ [T[0],1] ]
else:
  tmp=T[0]
  cnt=1
  for i in range(1,N):
    if i==N-1:
      if T[i]==T[i-1]:
        cnt+=1
        U.append([tmp,cnt] )
      else:
        U.append([tmp,cnt] )
        U.append([T[i],1])
    else:
      if T[i]==T[i-1]:
        cnt+=1
      else:
        U.append([tmp,cnt] )
        tmp=T[i]
        cnt=1

summ=0
for j in range(len(U)):
  summ += U[j][1]
  U[j][1]=summ
if U[0][0]==0:
  U.insert(0,[1,0])
  U.insert(0,[0,0])
else:
  U.insert(0,[0,0])

#print(U)
maxi=0
  
for p,q in enumerate(U):
  if q[0]==1:
    pass
  else:
    right=min(p+K*2+1,len(U)-1)
    diff=U[right][1]-U[p][1]
    maxi=max(diff,maxi)
    #print(p,right,diff)
print(maxi)