N,M,X = map(int,input().split())
A = list(map(int,input().split()))
L = [0]*(N+1)

for a in A:
  L[a]+=1

print(min(sum(L[:X]),sum(L[X+1:N])))