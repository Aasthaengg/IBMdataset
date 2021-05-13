N, X = map(int, input().split())
L = list(map(int, input().split()))
D = [0]*(N+1)
result = 1
for i in range(N):
  D[i+1] = D[i]+L[i]
  if D[i+1]<=X:
    result += 1
print(result)