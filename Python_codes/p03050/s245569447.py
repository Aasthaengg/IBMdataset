N = int(input())

lim = int(N**0.5) + 1
ans = 0
for i in range(1, lim):
    if N % i == 0:
        m = N // i - 1
        if i < m:
            ans += m
print(ans)
