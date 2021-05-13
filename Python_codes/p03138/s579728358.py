N, K = map(int,input().split())
A = list(map(int,input().split()))
L = [0 for _ in range(40)]
for a in A:
    for i in range(40):
        L[i] += a & 1
        a >>= 1
L.reverse()
K = '{:040b}'.format(K)
dp1 = [0 for _ in range(41)]
dp2 = [0 for _ in range(41)]

for i in range(40):
    dp1[i+1] += 2 * dp1[i]
    if K[i] == '0':
        dp1[i+1] += L[i]
    else:
        dp1[i+1] += N - L[i]
    if dp2[i] != 0:
        dp2[i+1] = 2 * dp2[i] + max(L[i], N - L[i])
    if K[i] == '1':
        dp2[i+1] = max(dp2[i+1], 2 * dp1[i] + L[i])

ans = max(dp1[40], dp2[40])

print(ans)