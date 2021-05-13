N,M=map(int,input().split())
K=list(map(int,input().split()))
L=sorted(K)
S=0
for i in range(N):
  S+=L[i]
if L[N-M]*4*M<S:
  print("No")
else:
  print("Yes")
