import sys
from collections import deque

def solve():
    input = sys.stdin.readline
    N = int(input())
    Edge = [[] for _ in range(N)]
    for _ in range(N-1):
        a, b, c = map(int, input().split())
        Edge[a-1].append((b-1, c))
        Edge[b-1].append((a-1, c))
    Q, K = map(int, input().split())
    Ans = [0] * Q
    Dist = [-1] * N
    q = deque()
    q.append((K-1, K-1, 0))
    while q:
        nowN, pre, dist = q.popleft()
        if Dist[nowN] == -1:
            Dist[nowN] = dist
            for nextN, cost in Edge[nowN]:
                if nextN != pre: q.append((nextN, nowN, dist + cost))
    for i in range(Q):
        x, y = map(int, input().split())
        Ans[i] = Dist[x-1] + Dist[y-1]

    print(*Ans, sep="\n")
    return 0

if __name__ == "__main__":
    solve()