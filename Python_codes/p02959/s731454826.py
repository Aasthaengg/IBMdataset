N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

assert len(A) == N + 1
assert len(B) == N

count = 0
for i in range(N-1, -1, -1):
  cost2 = min(A[i + 1], B[i])
  A[i+1] -= cost2
  cost1 = min(A[i], B[i] - cost2)
  A[i] -= cost1
  count += cost1 + cost2
print(count)