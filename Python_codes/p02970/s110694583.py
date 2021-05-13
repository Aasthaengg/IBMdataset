n, d = map(int, input().split())
ans = n // (2 * d + 1)
if ans * (2 * d + 1) < n:
    print(ans + 1)
else:
    print(ans)