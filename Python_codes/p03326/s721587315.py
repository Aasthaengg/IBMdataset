import sys
input = sys.stdin.readline
# sys.setrecursionlimit(10 ** 6)
# MOD = 10 ** 9 + 7
INF = float("inf")


def main():
    n, m = map(int, input().split())
    l = [tuple(map(int, input().split())) for _ in range(n)]
    ans = -INF
    for bit in range(1 << 3):
        sign = [0] * 3
        for i in range(3):
            if bit >> i & 1:
                sign[i] = 1
        sign = [i if i else -1 for i in sign]
        total = []
        for x, y, z in l:
            total.append(sign[0] * x + sign[1] * y + sign[2] * z)
        total.sort(reverse=True)
        ans = max(ans, sum(total[:m]))
    print(ans)


if __name__ == '__main__':
    main()
