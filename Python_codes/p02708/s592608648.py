n, k = map(int, input().split())

ans = 0
for i in range(k, n + 2):
    # print(i)
    smin = int(0.5 * i * (2 * 0 + (i - 1) * 1))
    smax = int(0.5 * i * (2 * (n + 1 - i) + (i - 1) * 1))
    s = smax - smin + 1
    # print("s", s)
    ans += s
    ans = ans % (7 + 10 ** 9)
print(ans)
