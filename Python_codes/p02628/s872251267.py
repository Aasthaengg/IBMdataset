N, K = map(int, input().split()) 
A = sorted(map(int, input().split()))
ans = 0

for i in range(K):
  ans = ans + A[i]

print(ans)