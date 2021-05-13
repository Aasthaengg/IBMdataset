N = int(input())
T = list(map(int,input().split()))
M = int(input())
A = sum(T)

for m in range(M):
  P,X = map(int,input().split())
  print(A-T[P-1]+X)