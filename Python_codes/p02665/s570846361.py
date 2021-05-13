def main():
    n = int(input())
    a = list(map(int, input().split()))
    lim = [None]*(n+1)
    f = True
    lim[0] = 1 - a[0]
    for i in range(1, n+1):
        lim[i] = lim[i-1]*2
        lim[i] -= a[i]
    ans = 0
    pre = 0
    for i in reversed(range(n+1)):
        if (pre+1)//2 > lim[i]:
            f = False
            break
        x = a[i] + min(lim[i], pre)
        ans += x
        pre = x
    if f:
        print(ans)
    else:
        print(-1)

if __name__ == "__main__":
    main()