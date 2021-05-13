N, K = map(int, input().split())
V = list(map(int, input().split()))

max_ = 0
for a in range(K + 1):
    for b in range(K - a + 1):
        if a + b > N:
            continue

        jwl = V[:a]
        jwl += V[N - b:]
        rmv = K - (a + b)
        jwl.sort()

        sum_ = sum(jwl)
        for i in range(min(rmv, len(jwl))):
            if jwl[i] >= 0:
                break

            sum_ -= jwl[i]

        max_ = max(max_, sum_)


print(max_)
