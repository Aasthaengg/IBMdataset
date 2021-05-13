
def solve(N, K):
    # N <= 10^5
    if K == 0:
        return N * N
    cnt = 0
    for b in range(K, N+1):
        q, r = divmod(N, b)
        cnt += max(0, b-K) * q + max(0, r - K + 1)
    return cnt

assert solve(5, 2) == 7
assert solve(10, 0) == 100
N, K = map(int, input().split())
print(solve(N, K))
