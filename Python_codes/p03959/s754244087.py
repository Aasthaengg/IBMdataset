MOD = 10**9 + 7
def main():
    n = int(input())
    t = list(map(int, input().split()))
    a = list(map(int, input().split()))
    h = [None]*n
    h[0] = t[0]
    for i in range(1, n):
        if t[i-1] < t[i]:
            h[i] = t[i]
    f = True
    if h[n-1] is not None and h[n-1] != a[n-1]:
        f = False
    if h[n-1] is None:
        h[n-1] = a[n-1]
    for i in reversed(range(n-1)):
        if a[i] > a[i+1]:
            if h[i] is None:
                h[i] = a[i]
            else:
                if h[i] != a[i]:
                    f = False
        if h[i] is not None and h[i] > a[i]:
            f = False
    if f:
        ans = 1
        for i in range(n):
            if h[i] is None:
                ans *= min(t[i], a[i])
                ans %= MOD
        print(ans % MOD)
    else:
        print(0)

if __name__ == "__main__":
    main()