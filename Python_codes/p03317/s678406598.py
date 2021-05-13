N, K = map(int, input().split())
A = [int(i) for i in input().split()]
A.sort()
for i in range(1, N):
    if A[i] != A[0]:
        idx = i
        break
# int((N - idx) / K)
if (N - idx) % (K - 1) == 0:
    print(int((N - idx) / (K - 1)))
else:
    print(int((N - idx) / (K - 1)) + 1)