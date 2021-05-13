def main():
    h, w, d = map(int, input().split())

    a = [None] * (h * w + 1)
    for i in range(1, h + 1):
        l = map(int, input().split())
        for j, k in enumerate(l, 1):
            a[k] = (i, j)

    c = [0] * (h * w + 1)
    for i in range(d + 1, h * w + 1):
        xb, yb = a[i-d]
        xn, yn = a[i]
        c[i] = c[i - d] + abs(xn - xb) + abs(yn - yb)

    q = int(input())
    res = []
    for _ in range(q):
        l, r = map(int, input().split())
        res.append(c[r] - c[l])

    ans = '\n'.join(map(str, res))
    print(ans)


if __name__ == '__main__':
    main()
