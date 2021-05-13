import sys
from collections import deque


def input():
    return sys.stdin.readline().strip()


MOD = 10 ** 9 + 7
sys.setrecursionlimit(20000000)
INF = float("inf")


def main():
    N = int(input())
    q = deque(["a"])
    cnt = 1
    answer = []
    while cnt <= N:
        d = q.popleft()

        if len(d) == N:
            answer.append(d)
        cnt = max(cnt, len(d))
        b = 0
        for i in range(cnt):
            if ord(d[i]) > b:
                b = ord(d[i])

        for i in range(ord("a"), b + 2):
            q.append(d + chr(i))
    answer.sort()
    print(*answer, sep="\n")


if __name__ == "__main__":
    main()
