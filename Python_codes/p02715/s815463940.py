MOD = 10**9 + 7


def main():
    N, K = (int(i) for i in input().split())
    g = [0]*(K+1)
    for k in range(1, K+1)[::-1]:
        cnt = K//k
        g[k] += pow(cnt, N, MOD)
        p = k
        while p + k <= K:
            p += k
            g[k] -= g[p]
        g[k] %= MOD
    ans = 0
    for i, g in enumerate(g[1:], start=1):
        ans += i*g
        ans %= MOD
    print(ans)


if __name__ == '__main__':
    main()
