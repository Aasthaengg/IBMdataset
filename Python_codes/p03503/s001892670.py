N=int(input())
F=[list(map(int,input().split())) for _ in range(N)]
P=[list(map(int,input().split())) for _ in range(N)]
import math
profit=-math.inf
for i in range(1,2**10):
  temp=0
  i=format(i,'b').rjust(10,'0')
  e=[]
  for j in range(10):
    if i[j]=='1':
      e.append(j)
  for k in range(N):
    count=0
    for l in range(len(e)):
      if F[k][e[l]]==1:
        count+=1
    temp+=P[k][count]
  profit=max(temp,profit)
print(profit)