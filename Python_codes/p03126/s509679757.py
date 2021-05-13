def actual(N, M, K, A):
    # 各人のAの積集合の要素数が答え
    s = set(A[0])

    for a in A[1:]:
        s &= set(a)

    return len(s)


N, M = map(int, input().split())

K = []
A = []

for _ in range(N):
    ka = list(map(int, input().split()))
    K.append(ka[0])
    A.append(ka[1:])

print(actual(N, M, K, A))
