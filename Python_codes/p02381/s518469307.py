while True:
    n = int(input())
    if n == 0:
        break
    else:
        a = list(map(int, input().split()))
        m = sum(a)/n
        sigma = 0
        for i in range(n):
            sigma += (a[i] - m)**2
        bun = sigma/n
        ans = bun**(1/2)
    print(ans)
