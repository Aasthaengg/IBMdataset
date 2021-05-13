N, D = map(int, input().split())

m = 2 * D + 1
if N % m == 0:
    ans = N // m
    print(ans)
else:
    ans = N // m + 1
    print(ans)