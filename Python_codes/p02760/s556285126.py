A1=list(map(int,input().split()))
A2=list(map(int,input().split()))
A3=list(map(int,input().split()))
N=int(input())
for i in range(N):
  b=int(input())
  if b in A1:
    t=A1.index(b)
    A1[t]=0
  elif b in A2:
    t=A2.index(b)
    A2[t]=0
  elif b in A3:
    t=A3.index(b)
    A3[t]=0
if sum(A1)==0 or sum(A2)==0 or sum(A3)==0:
  print("Yes")
else:
  for j in range(3):
    if A1[j]+A2[j]+A3[j]==0:
      print("Yes")
      break
  else:
    if A1[0]+A2[1]+A3[2]==0 or A1[2]+A2[1]+A3[0]==0:
      print("Yes")
    else:
      print("No")