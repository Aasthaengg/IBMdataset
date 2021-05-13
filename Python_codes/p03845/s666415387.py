N=int(input())
T=list(map(int,input().split()))
S=sum(T)
M=int(input())
for i in range(M):
  P, X = map(int,input().split())
  diff = T[P-1]-X
  print(S-diff)