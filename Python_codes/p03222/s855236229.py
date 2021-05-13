import itertools


h, w, k = map(int, input().split())

DP = [0] * w
DP[0] = 1
mod = 10**9 + 7

patterns = []

for line_count in range(w):
    candidates = itertools.combinations(range(w-1), line_count)

    for pattern in candidates:
        usable = True
        prev = 10

        for num in pattern:
            if num == prev + 1:
                usable = False
                break
            else:
                prev = num

        if usable:
            patterns.append(pattern)

for i in range(h):
    next_DP = [0] * w

    for pattern in patterns:
        straight = set(range(w))
        for line in pattern:
            next_DP[line] += DP[line+1]
            next_DP[line] %= mod
            next_DP[line+1] += DP[line]
            next_DP[line+1] % mod
            straight.discard(line)
            straight.discard(line+1)

        for line in straight:
            next_DP[line] += DP[line]
            next_DP[line] %= mod

    DP = next_DP.copy()

ans = DP[k-1]
print(ans%mod)