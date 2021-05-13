def main():
    from collections import deque
    from math import ceil
    n, h, *ab = map(int, open(0).read().split())
    a = ab[::2]
    *b, = map(lambda x: -x, ab[1::2])
    c = a + b
    c.sort(key=lambda x: abs(x), reverse=True)

    q = deque(c)
    cnt = 0
    while h > 0:
        cnt += 1
        x = q.popleft()
        h -= abs(x)
        if x > 0:
            cnt += ceil(h / x)
            break

    print(cnt)


if __name__ == '__main__':
    main()
