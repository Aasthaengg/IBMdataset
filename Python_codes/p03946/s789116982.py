def main():
    from heapq import heappush

    inf = 1 << 30

    N, T = map(int, input().split())
    *A, = map(int, input().split())

    h = [inf]
    ma = -1
    cnt = 0
    for x in A:
        d = x - h[0]
        if ma < d:
            ma = d
            cnt = 1
        elif ma == d:
            cnt += 1
        heappush(h, x)

    print(cnt)


if __name__ == '__main__':
    main()
