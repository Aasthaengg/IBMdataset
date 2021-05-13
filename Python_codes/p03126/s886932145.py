N,M=map(int,input().split())
R=set(range(1,M+1))
for i in range(N):
  L=list(map(int,input().split()))
  R=set(L[1:])&R
print(len(R))