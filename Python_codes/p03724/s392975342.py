N, M = map(int, input().split())
A = [0]*(N+1)
for _ in range(M):
  a, b = map(int, input().split())
  A[a] = (A[a]+1)%2
  A[b] = (A[b]+1)%2
print("YES" if len(list(filter(lambda x:x==1, A))) < 1 else "NO")