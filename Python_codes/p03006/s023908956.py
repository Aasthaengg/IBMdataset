def main():
    from collections import Counter, namedtuple

    pt = namedtuple('pt', 'x y')

    def delta(a: pt, b: pt) -> pt:
        x = a.x - b.x
        y = a.y - b.y
        if (x < 0) or (x == 0 and y < 0):
            x = -x
            y = -y
        return pt(x=x, y=y)

    n = int(input())
    if n == 1:
        # deltaが計算できないので、
        # 別処理する
        print(1)
        return

    ps = [pt(*map(int, input().split())) for _ in range(n)]

    c = Counter(
        delta(a, b)
        for i, a in enumerate(ps)
        for j, b in enumerate(ps)
        if i < j
    )

    ma = max(c.values())

    print(n - ma)


if __name__ == '__main__':
    main()
