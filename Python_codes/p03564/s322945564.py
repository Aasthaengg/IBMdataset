N = int(input())
K = int(input())

ans = 10**18
for state in range(1 << N):
    now = 1
    for d in range(N):
        if (state & (1 << d)) == 0:
            now *= 2
        else:
            now += K
    ans = min(ans, now)
print(ans)
