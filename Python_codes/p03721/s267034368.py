import bisect

N, K = map(int, input().split())
A = []; B = [0]

for i in range(N):
    a, b = map(int, input().split())
    A.append([a, b])
A.sort()
for i in range(N):
    B.append(A[i][1] + B[i])

ans = bisect.bisect_left(B, K) - 1
print(A[ans][0])