n, *A = map(int, open(0).read().split())

ans = s = r = 0
for l in range(n):
    while r < n and s & A[r] == 0:
        s += A[r]
        r += 1
    s -= A[l]
    ans += r-l
print(ans)