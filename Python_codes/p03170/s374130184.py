N, K = map(int, input().split())
A = list(map(int, input().split()))
sorted(A)
DP = [-1] * (K+1)
for i in range(K+1):
    if i < A[0]:
        DP[i] = False
    else:
        for j in A:
            if i - j <= 0:
                DP[i] = False
            if not DP[i-j]:
                DP[i] = True
                break
            DP[i] = False
if DP[K]:
    print('First')
else:
    print('Second')
