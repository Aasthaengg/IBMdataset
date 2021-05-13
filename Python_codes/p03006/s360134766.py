def main():
    import sys
    input = sys.stdin.buffer.readline
    N = int(input())
    XY = [[int(i) for i in input().split()] for j in range(N)]
    XY.sort()
    from collections import Counter
    c = Counter()
    for i in range(N-1):
        for j in range(i+1, N):
            p = XY[j][0] - XY[i][0]
            q = XY[j][1] - XY[i][1]
            c[(p, q)] += 1
    ans = N - (c.most_common()[0][1] if c else 0)
    print(ans)


if __name__ == '__main__':
    main()
