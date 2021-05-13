def main():
    h, w = map(int, input().split())
    s = ["#" * (w + 2)]
    for _ in range(h):
        s.append("#" + input() + "#")
    s.append("#" * (w + 2))

    b = [[0] * (w + 2) for _ in range(h + 2)]
    for hi in range(h + 2):
        for wi in range(w + 2):
            if s[hi][wi] == ".":
                b[hi][wi] = 1

    u = [[0] * (w + 2) for _ in range(h + 2)]
    d = [[0] * (w + 2) for _ in range(h + 2)]
    l = [[0] * (w + 2) for _ in range(h + 2)]
    r = [[0] * (w + 2) for _ in range(h + 2)]

    for hi in range(1, h + 1):
        for wi in range(1, w + 1):
            if b[hi][wi]:
                u[hi][wi] = u[hi-1][wi] + 1
                l[hi][wi] = l[hi][wi-1] + 1

    for hi in range(h, 0, -1):
        for wi in range(w, 0, -1):
            if b[hi][wi]:
                d[hi][wi] = d[hi+1][wi] + 1
                r[hi][wi] = r[hi][wi+1] + 1

    ans = 0
    for hi in range(1, h + 1):
        for wi in range(1, w + 1):
            cnt = u[hi][wi] + d[hi][wi] + l[hi][wi] + r[hi][wi] - 3
            ans = max(ans, cnt)

    print(ans)


if __name__ == "__main__":
    main()
