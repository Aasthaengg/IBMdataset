def a_to_b(A):
    c = [0] * N
    for i, a in enumerate(A):
        lb = max(0, i - a)
        c[lb] += 1
        ub = i + a + 1
        if ub < N:
            c[ub] -= 1
    tmp = 0
    B = []
    for ci in c:
        tmp += ci
        B.append(tmp)
    return B


N, K = map(int, input().split())
A = list(map(int, input().split()))

ans = A
for _ in range(K):
    ans = a_to_b(ans)
    if sum(ans) == N ** 2:
        break

print(*ans)