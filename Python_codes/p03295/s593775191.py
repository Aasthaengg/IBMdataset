import sys

sys.setrecursionlimit(10 ** 6)
INF = float("inf")
MOD = 10 ** 9 + 7


def input():
    return sys.stdin.readline().strip()


def main():
    N, M = map(int, input().split())
    AB = []
    for _ in range(M):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        AB.append((a, b))
    AB.sort(key=lambda x: x[0])

    cnt = 0
    end = INF
    for a, b in AB:
        if a >= end:
            cnt += 1
            end = b
        else:
            end = min(b, end)

    cnt += 1
    print(cnt)


if __name__ == "__main__":
    main()
