import sys
import itertools

input = sys.stdin.readline


def main():
    N, K = [int(x) for x in input().split()]
    XY = [[int(x) for x in input().split()] for _ in range(N)]

    xset = set()
    yset = set()

    for x, y in XY:
        xset.add(x)
        yset.add(y)

    xlist = list(xset)
    ylist = list(yset)

    ans = float("inf")

    for a, b in itertools.combinations(range(len(xlist)), 2):
        maxx = max(xlist[a], xlist[b])
        minx = min(xlist[a], xlist[b])

        for c, d in itertools.combinations(range(len(ylist)), 2):
            maxy = max(ylist[c], ylist[d])
            miny = min(ylist[c], ylist[d])

            cnt = 0
            for x, y in XY:
                if minx <= x <= maxx and miny <= y <= maxy:
                    cnt += 1

            if cnt >= K:
                ans = min(ans, (maxx - minx) * (maxy - miny))

    print(ans)


if __name__ == '__main__':
    main()
