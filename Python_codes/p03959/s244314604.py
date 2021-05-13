MOD = 1000000007

N = int(input())
T = list(map(int, input().split()))
A = list(map(int, input().split()))

L1 = [0 for _ in range(N)]
R1 = [0 for _ in range(N)]
L2 = [0 for _ in range(N)]
R2 = [0 for _ in range(N)]

tmp1 = 1
tmp2 = 1

for i in range(N):
    if tmp1 < T[i]:
        L1[i] = T[i]
        R1[i] = T[i]
        tmp1 = T[i]
    elif tmp1 == T[i]:
        L1[i] = 1
        R1[i] = tmp1
    else:
        print(0)
        break
    if tmp2 < A[~i]:
        L2[~i] = A[~i]
        R2[~i] = A[~i]
        tmp2 = A[~i]
    elif tmp2 == A[~i]:
        L2[~i] = 1
        R2[~i] = tmp2
    else:
        print(0)
        break
else:
    res = 1
    for i in range(N):
        res *= max(min(R1[i], R2[i]) - max(L1[i], L2[i]) + 1, 0)
        res %= MOD
    print(res)