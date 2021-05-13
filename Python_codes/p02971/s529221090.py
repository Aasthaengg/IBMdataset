N=int(input())
A=[]
for i in range(N):
  a=int(input())
  A.append(a)
import copy
B=copy.copy(A)
B.sort()
max=B[-1]
max2=B[-2]

if max==max2:
  for i in range(N):
    print(max)
else:
  ind=A.index(max)
  for i in range(N):
    if i==ind:
      print(max2)
    else:
      print(max)