N=int(input())
A=list(map(int,input().split()))
S={}
for i in range(N):
  if A[i] in S: S[A[i]]+=1
  else: S[A[i]]=1
d=0
for i in S.values():
  d+=(i-1)
print(len(set(A))-d%2)