mod = 10 ** 9 + 7

N = int(input())
T = [int(i) for i in input().split()]
A = [int(i) for i in input().split()]

HT = [False] * N
for i in range(1, N):
    if T[i - 1] < T[i]:
        HT[i] = True
HT[0] = True

HA = [False] * N
for i in range(N - 1):
    if A[i] > A[i + 1]:
        HA[i] = True
HA[-1] = True

ans = 1
for i in range(N):
    if HT[i] and HA[i]:
        ans *= 1 if T[i] == A[i] else 0
    elif HT[i]:
        ans *= 1 if T[i] <= A[i] else 0
    elif HA[i]:
        ans *= 1 if T[i] >= A[i] else 0
    else:
        ans = (ans * min(T[i], A[i])) % mod
    if ans == 0:
        break
print(ans)
