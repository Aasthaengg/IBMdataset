import heapq
import itertools
import sys

input = sys.stdin.readline

def main():

    n,m,r = map(int,input().split())
    R = list(map(int,input().split()))
    for i in range(r):
        R[i] -= 1

    roots = [[] for _ in range(n)]
    for _ in range(m):
        a,b,c = map(int,input().split())
        roots[a-1].append((b-1, c))
        roots[b-1].append((a-1, c))

    def dijkstra(edges, s):
        hq = []
        d = [-1] * n
        d[s] = 0
        heapq.heappush(hq, (0, s))
        while hq:
            d1, p = heapq.heappop(hq)
            for p2, d2 in edges[p]:
                if d[p2] == -1 or d[p2] > d1 + d2:
                    d[p2] = d1 + d2
                    heapq.heappush(hq, (d1+d2, p2))
        return d

    ans = 10**10
    d = []

    for i in range(n):
        d1 = dijkstra(roots, i)
        d.append(d1)

    ptr = list(itertools.permutations(R, len(R))) # 順列列挙 5P3

    for i in ptr:
        tmp = 0
        for j in range(len(i) - 1):
            tmp += d[i[j]][i[j+1]]
        ans = min(ans, tmp)

    print(ans)

if __name__ == '__main__':
    main()
