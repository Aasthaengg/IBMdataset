def resolve():
    n = int(input())
    a = sorted(map(int, input().split()))

    cost = float("INF")
    mn = 0
    mx = a[-1]
    for aa in a[:-1]:
        tmp = abs(mx - aa * 2)
        if tmp < cost:
            cost = tmp
            mn = aa
    print(mx, mn)


if __name__ == "__main__":
    resolve()
