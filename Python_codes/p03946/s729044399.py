from collections import defaultdict

N, T = map(int, input().split())
A = tuple(map(int, input().split()))

B = defaultdict(int)
am = A[0]
for i in range(1, N):
    B[A[i] - am] += 1
    am = min(am, A[i])

print(B[max(B)])
