def main():
    N, K = map(int, input().split())
    dots = [tuple(map(int, input().split())) for _ in range(N)]
    
    xs = set()
    ys = set()
    for x, y in dots:
        xs.add(x)
        ys.add(y)
    
    xs = sorted(xs)
    ys = sorted(ys)

    def isOK(l, r, d, u):
        num = sum([l <= x and x <= r and d <= y and y <= u for x, y in dots])
        return num >= K

    ans = 4 * 10 ** 18
    for i, x1 in enumerate(xs):
        for x2 in xs[i+1:]:
            for j, y1 in enumerate(ys):
                for y2 in ys[j+1:]:
                    area = (x2-x1)*(y2-y1)
                    if isOK(x1, x2, y1, y2):
                        ans = min(ans, area)
    print(ans)


if __name__ == "__main__":
    main()