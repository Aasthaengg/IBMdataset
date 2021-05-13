import sys

input = sys.stdin.readline
INF = float("inf")


def main():
    N = int(input())
    h = list(map(int, input().split()))

    h += [0]
    N += 1
    ans = 0
    while True:
        l = 0
        min_h = INF
        for r in range(N):
            if h[r] == 0:
                if min_h == INF:
                    l += 1
                else:
                    for i in range(l, r):
                        h[i] -= min_h
                    ans += min_h
                    l = r + 1
                    min_h = INF
            else:
                if h[r] < min_h:
                    min_h = h[r]
        if sum(h) == 0:
            break

    print(ans)


if __name__ == "__main__":
    main()
