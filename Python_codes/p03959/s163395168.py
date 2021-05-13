MOD = 10**9 + 7

N = int(input())
Ts = list(map(int, input().split()))
As = list(map(int, input().split()))

minTs, maxTs = [1]*N, [10**9]*N
minAs, maxAs = [1]*N, [10**9]*N

minTs[0] = maxTs[0] = Ts[0]
for i in range(1, N):
    if Ts[i-1] < Ts[i]:
        minTs[i] = maxTs[i] = Ts[i]
    else:
        maxTs[i] = Ts[i]

minAs[-1] = maxAs[-1] = As[-1]
for i in reversed(range(N-1)):
    if As[i] > As[i+1]:
        minAs[i] = maxAs[i] = As[i]
    else:
        maxAs[i] = As[i]

ans = 1
for minT, maxT, minA, maxA in zip(minTs, maxTs, minAs, maxAs):
    minH = max(minT, minA)
    maxH = min(maxT, maxA)
    ans *= max(0, maxH - minH + 1)
    ans %= MOD
print(ans)
