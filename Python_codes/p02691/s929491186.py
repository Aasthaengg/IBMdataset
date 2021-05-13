from collections import defaultdict

N = int(input())
A = list(map(int, input().split()))
B = defaultdict(int)
C = defaultdict(int)

for i in range(N):
  B[A[i]+i+1] += 1
  C[-A[i]+i+1] += 1

ans = 0

for x in B.keys():
  ans += B[x] * C[x]

print(ans)