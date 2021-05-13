K = int(input())
A = [int(i) for i in input().split()]
A.reverse()

# L: 最小の生存人数
# H: 最大の生存人数
L, H = 2, 2
for i in range(K):
    # [L,H]で最小のA[i]の倍数
    MIN = (L + A[i] - 1) // A[i] * A[i]
    # [L,H]で最大のA[i]の倍数
    MAX = H // A[i] * A[i]

    if L <= MIN <= H:
        L = MIN
        H = MAX + A[i] - 1
    else:
        print(-1)
        exit()

print(L,H)