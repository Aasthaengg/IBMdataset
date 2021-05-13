N=int(input())
A=list(map(int,input().split()))
B=[]
C=[]
D=[]

for i in range(N):
  if A[i]<0:
    B.append(A[i])
  elif A[i]==0:
    C.append(A[i])
  else:
    D.append(A[i])

ans=[]
anss=0

if len(B)>0 and len(D)>0:
  for i in C:
    ans.append((B[0],0))
  for i in range(len(D)-1):
    ans.append((B[0],D[i]))
    B[0]-=D[i]
  for i in range(len(B)):
    ans.append((D[-1],B[i]))
    D[-1]-=B[i]
  anss=D[-1]

elif len(C)>0:
  for i in range(len(C)-1):
    ans.append((0,0))
  for i in B:
    ans.append((anss,i))
    anss-=i
  if(len(D)>0):
    for i in range(len(D)-1):
      ans.append((anss,D[i]))
      anss-=D[i]
    ans.append((D[-1],anss))
    anss=D[-1]-anss

else:
  E=sorted(B,reverse=True)+sorted(D)
  anss=E[0]
  for i in range(len(E)-2):
    ans.append((anss,E[i+1]))
    anss-=E[i+1]
  if anss<=0:
    ans.append((E[-1],anss))
    anss=E[-1]-anss
  else:
    ans.append((anss,E[-1]))
    anss-=E[-1]

print(anss)
for i in ans:
  print(*i)