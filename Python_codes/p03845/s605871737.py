import copy

N=int(input())
T=list(map(int,input().split()))
M=int(input())
for i in range(M):
  check=copy.deepcopy(T)
  P,X=map(int,input().split())
  check[P-1]=X
  print(sum(check))
