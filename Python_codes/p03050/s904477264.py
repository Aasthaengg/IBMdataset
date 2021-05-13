N = int(input())
ans = 0
for m in range(1,10**6):
    if N // m == N % m:
        ans += m
for k in range(1,10**6):
    if (N-k) % k == 0:
        m = (N-k) // k
        if m > 10**6:
            ans += m
print(ans)