from collections import Counter
n=int(input())
A=list(map(int,input().split()))
A=Counter(A)

S=[]
for i,j in A.items():
  if j>=2:
    S.append(i)
S=list(set(S))
S.sort()
if len(S)>=2:
  ans=S[-1]*S[-2]
else:
  print(0)
  exit()

Q=[]

for i,j in A.items():
  if j>=4:
    Q.append(i)
if Q==[]:
  print(ans)
  exit()
print(max(ans, (max(Q))**2))
