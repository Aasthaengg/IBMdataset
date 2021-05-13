import heapq
import sys
from collections import deque


def input():
    return sys.stdin.readline().strip()


sys.setrecursionlimit(20000000)

MOD = 10 ** 9 + 7
INF = float("inf")


def main():
    N = int(input())
    tree = [[] for _ in range(N)]
    edge = deque([])

    for _ in range(N - 1):
        a, b = map(int, input().split())
        tree[a - 1].append(b - 1)
        tree[b - 1].append(a - 1)
        edge.append((a - 1, b - 1))

    C = list(map(int, input().split()))
    C.sort()
    D = []
    for c in C:
        heapq.heappush(D, -c)

    answer = [0] * N
    a, b = edge.popleft()
    c = heapq.heappop(D) * (-1)
    d = heapq.heappop(D) * (-1)
    if len(tree[a]) == 0:
        answer[a] = c
        answer[b] = d
    else:
        answer[a] = d
        answer[b] = c

    new_node = deque([])
    for n in tree[a]:
        new_node.append(n)
    for n in tree[b]:
        new_node.append(n)

    while new_node:
        s = new_node.popleft()
        if answer[s] == 0:
            answer[s] = heapq.heappop(D) * (-1)
        for n in tree[s]:
            if answer[n] == 0:
                new_node.append(n)

    print(sum(C[:-1]))
    print(*answer)


if __name__ == "__main__":
    main()
