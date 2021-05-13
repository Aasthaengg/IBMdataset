MOD = 10**9 + 7


def dup(x, y):
    return x + x*y + 1 - y**2


def main():
    n, m = map(int, input().split())
    x = list(map(int, input().split()))
    y = list(map(int, input().split()))
    tmp = 0
    for i in range(n-1):
        tmp = (tmp + (x[i+1] - x[i]) * dup(n-2, i)) % MOD
    ans = 0
    for i in range(m-1):
        ans = (ans + (y[i+1] - y[i]) * dup(m-2, i) * tmp) % MOD
        ans = ans % MOD
    print(ans)


if __name__ == "__main__":
    main()
