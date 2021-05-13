N, K = map(int, input().split())

qs = 0
for i in range(1, N+1):
    if i >= K:
        qs += 1/N
    elif i < K:
        q = 1/N
        while i < K:
            q *= 1/2
            i *= 2
        qs += q
print(qs)