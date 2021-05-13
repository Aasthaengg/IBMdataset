# でつoO(YOU PLAY WITH THE CARDS YOU'RE DEALT..)
from heapq import heappush, heappop
import sys
def main(N, M, G, S, T):
    INF = 10**10
    dp = [[INF for _ in range(N)] for __ in range(3)]
    dp[0][S] = 0
    q = [(0, S)]
    while q:
        d, v = heappop(q)
        for to in G[v]:
            if d + 1 >= dp[(d + 1) % 3][to]: continue
            dp[(d + 1) % 3][to] = d + 1
            heappush(q, (d + 1, to))
    print(dp[0][T] // 3 if dp[0][T] < INF else -1)

if __name__ == '__main__':
    input = sys.stdin.readline
    N, M = map(int, input().split())
    G = [[] for _ in range(N)]
    for _ in range(M):
        x, y = map(int, input().split())
        x, y = x - 1, y - 1
        G[x].append(y)
    S, T = map(lambda x: int(x) - 1, input().split())
    main(N, M, G, S, T)
