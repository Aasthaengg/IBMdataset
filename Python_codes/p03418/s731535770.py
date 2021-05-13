def solve(n, k):
    cnt = 0
    if k == 0:
        return n * n
    for b in range(k + 1, n + 1):
        p = n // b
        r = n % b
        cnt += p * (b - k)
        if r >= k:
            cnt += r - k + 1
    return cnt

n, k = map(int, input().split())
print(solve(int(n), int(k)))
