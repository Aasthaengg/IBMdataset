n, k = map(int, input().split())
x = list(map(int, input().split()))
k -= 1
ans = 10**9

for i in range(n - k):
    l = x[i]
    r = x[i + k]
    if l < 0:
        if r < 0:
            ref = -l
        else:
            ref = min(l*-2 + r, -l + r*2)
    else:
        ref = r
    ans = min(ans, ref)

print(ans)