a = list(map(int, input().split()))
if a[0] * a[1] * a[2] % 2:
    ans = 10 ** 19
    for i in range(3):
        ans = min(ans, min(a[i], a[(i + 1) % 3]) * a[(i + 2) % 3])
    print(ans)
else:
    print(0)
