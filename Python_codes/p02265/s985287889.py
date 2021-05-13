import sys, os, math, bisect, itertools, collections, heapq, queue
# from scipy.sparse.csgraph import csgraph_from_dense, floyd_warshall
from decimal import Decimal
from collections import defaultdict, deque
import copy

sys.setrecursionlimit(10000000)

ii = lambda: int(sys.stdin.buffer.readline().rstrip())
il = lambda: list(map(int, sys.stdin.buffer.readline().split()))
fl = lambda: list(map(float, sys.stdin.buffer.readline().split()))
iln = lambda n: [int(sys.stdin.buffer.readline().rstrip()) for _ in range(n)]

iss = lambda: sys.stdin.buffer.readline().decode().rstrip()
sl = lambda: list(map(str, sys.stdin.buffer.readline().decode().split()))
isn = lambda n: [sys.stdin.buffer.readline().decode().rstrip() for _ in range(n)]

lcm = lambda x, y: (x * y) // math.gcd(x, y)

MOD = 10 ** 9 + 7
MAX = float('inf')


def main():
    if os.getenv("LOCAL"):
        sys.stdin = open("input.txt", "r")

    N = ii()
    que = deque()

    for n in range(N):
        cmd = sl()
        if cmd[0] == 'insert':
            que.appendleft(cmd[1])
        elif cmd[0] == 'delete' and cmd[1] in que:
            que.remove(cmd[1])
        elif cmd[0] == 'deleteFirst' and len(que) > 0:
            que.popleft()
        elif cmd[0] == 'deleteLast' and len(que) > 0:
            que.pop()
    print(*que)


if __name__ == '__main__':
    main()

