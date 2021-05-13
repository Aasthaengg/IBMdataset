def diverta19_d():
    N = int(input())
    ans = 0
    for i in range(1, min(N, 10**6+1)):
        d, m = divmod(N-i, i)
        if m == 0 and i < d:
            ans += d
    print(ans)

diverta19_d()