def main():
    n, k = map(int, input().split())
    w = []
    for i in range(n):
        w.append(int(input()))
    minp = max(w)
    maxp = sum(w)
    p = (minp + maxp) // 2
    while minp < maxp:
        l = w[0]
        t = 1
        for ww in w[1:]:
            if l + ww <= p:
                l += ww
            else:
                t += 1
                l = ww
        if t > k:
            minp = p + 1
        else:
            maxp = p
        p = (minp + maxp) // 2
    print(p)


if __name__ == '__main__':
    main()

