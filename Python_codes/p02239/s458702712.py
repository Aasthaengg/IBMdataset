from collections import deque
import sys


def bfs():
    color[0] = "GRAY"
    d[0] = 0
    Q.append(0)
    while len(Q) != 0:
        u = Q.popleft()
        for v in range(n):
            if M[u][v] and color[v] == "WHITE":
                color[v] = "GRAY"
                d[v] = d[u] + 1
                Q.append(v)
        color[u] = "BLACK"


if __name__ == "__main__":
    n = int(sys.stdin.readline())
    M = [[0] * n for i in range(n)]
    color = ["WHITE"] * n
    d = [-1] * n
    Q = deque()
    for inp in sys.stdin.readlines():
        inp = list(map(int, inp.split()))
        for i in inp[2:]:
            M[inp[0]-1][i-1] = 1
    bfs()
    for i in range(n):
        print(i+1, d[i])