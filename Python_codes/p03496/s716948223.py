def main():
    N = int(input())
    A = tuple(map(int, input().split()))

    a = list(A)
    m = 0
    xy = []
    apnd = xy.append
    if min(a) == max(a):
        print(0)
        return
    elif min(a) < 0 and max(a) >= 0:
        if abs(min(a)) > max(a):
            x = min(a)
        else:
            x = max(a)
        idx = a.index(x)
        for i, j in enumerate(a):
            if j != x:
                a[i] += x
                m += 1
                apnd((idx + 1, i + 1))

    if min(a) >= 0:
        for i in range(N - 1):
            a[i+1] += a[i]
            m += 1
            apnd((i + 1, i + 2))
    elif max(a) < 0:
        for i in range(N - 1, 0, -1):
            a[i-1] += a[i]
            m += 1
            apnd((i + 1, i))

    print(m)
    for x, y in xy:
        print(x, y)

main()
