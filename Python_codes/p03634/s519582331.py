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
    q = deque()
    Dist = [-1] * N
    q.append((K-1, K-1, 0))
    while q:
        nowN, preN, nD = q.popleft()
        if Dist[nowN] == -1:
            Dist[nowN] = nD
            for e, add in Edge[nowN]:
                if e != preN: q.append((e, nowN, nD + add))
    Ans = [None] * Q
    for i in range(Q):
        x, y = map(int, input().split())
        Ans[i] = str(Dist[x-1] + Dist[y-1])
    print("\n".join(Ans))

    return 0

if __name__ == "__main__":
    solve()
