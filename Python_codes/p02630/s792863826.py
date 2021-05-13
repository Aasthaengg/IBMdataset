import collections
N=int(input())
A=list(map(int,input().split()))
Q=int(input())
M=collections.Counter(A)
ans=0
for j in M.items():
  ans+=j[0]*j[1]
for i in range(Q):
  B,C=map(int,input().split())
  ans+=(C-B)*M[B]
  M[C]+=M[B]
  M[B]=0
  print(ans)