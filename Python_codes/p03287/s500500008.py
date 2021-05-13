from collections import defaultdict
n,m=map(int,input().split())
A=list(map(int,input().split()))
B=[0]
for i in range(n):
  B.append((B[-1]+A[i])%m)
C=defaultdict(int)
for i in range(n+1):
  C[B[i]]+=1
ans=0
for key in C.values():
  ans+=key*(key-1)//2
print(ans)