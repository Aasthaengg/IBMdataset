def solve():
    if N == 0:
        if A[0] == 1:
            return 1
        else:
            return -1

    if A[0] != 0:
        return -1

    tot = sum(A)
    cur = 1
    ans = 1
    for i in range(1, N + 1):
        cur *= 2
        if cur < A[i]:
            return -1
        tmp = min(cur, tot)
        ans += tmp
        cur = tmp - A[i]
        tot -= A[i]
    return ans


N, *A = map(int, open(0).read().split())
print(solve())
