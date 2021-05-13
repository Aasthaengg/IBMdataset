N,M = map(int,input().split())
B = set(m for m in range(1,1+M))

for n in range(N):
  A = list(map(int,input().split()))
  B&=set(A[1:])

print(len(B))