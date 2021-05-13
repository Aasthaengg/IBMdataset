N,M = map(int, input().split())

A = [0 for _ in range(N)]
for _ in range(M):
  a,b = map(int, input().split())
  a,b = a-1, b-1
  A[a] += 1
  A[b] += 1
  
for a in A:
  if a%2 == 1:
    print("NO")
    exit(0)
print("YES")