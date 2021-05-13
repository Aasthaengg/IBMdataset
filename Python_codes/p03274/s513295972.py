n, k = map(int, input().split())
x = list(map(int, input().split()))

ans = 10**9

for i in range(n - k + 1):
    if x[i] < 0:
        if x[i + k - 1] < 0:
            ref = -x[i]
        else:
            ref = min(x[i]*-2 + x[i + k - 1], -x[i] + x[i + k - 1]*2)
    else:
        ref = x[i + k - 1]
    ans = min(ans, ref)

print(ans)