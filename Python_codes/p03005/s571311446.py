n, k = map(int, input().split())

if k == 1:
    print(0)
else:
    mx = n - k + 1
    ans = mx - 1
    print(ans)
