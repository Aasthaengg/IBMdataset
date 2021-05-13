N=int(input())
P=list(map(int,input().split()))
Q=sorted(P)
X=0
for i in range(N):
  if P[i]!=Q[i]:
    X+=1
if X==2 or X==0:
  print('YES')
else:
  print('NO')