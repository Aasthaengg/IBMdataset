import sys
from collections import deque

sys.setrecursionlimit(10 ** 6)
INF = float("inf")
MOD = 10 ** 9 + 7


def input():
    return sys.stdin.readline().strip()


def main():
    N = int(input())

    for i in range(1, N + 1):
        if 2 * N == i * (i + 1):
            L = i
            break
    else:
        print("No")
        return

    ans = [[] for _ in range(L + 1)]
    used = [deque([]) for _ in range(L + 1)]
    no = deque(range(1, N + 1))

    for i in range(L + 1):
        if i == 0:
            for _ in range(L):
                j = no.popleft()
                ans[i].append(j)
                used[i].append(j)
        else:
            for j in range(i):
                k = used[j].popleft()
                ans[i].append(k)
            for _ in range(L - i):
                j = no.popleft()
                ans[i].append(j)
                used[i].append(j)

    print("Yes")
    print(L + 1)
    for a in ans:
        print(len(a), end=" ")
        print(*a, sep=" ")


if __name__ == "__main__":
    main()
