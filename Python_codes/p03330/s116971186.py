import sys
from collections import defaultdict
from heapq import heappush, heappop
def input(): return sys.stdin.readline().strip()


def main():
    N, C = map(int, input().split())
    D = [list(map(int, input().split())) for _ in range(C)]
    mod = [defaultdict(int), defaultdict(int), defaultdict(int)]
    for i in range(N):
        c = list(map(int, input().split()))
        for j in range(N):
            mod[(i + j) % 3][c[j] - 1] += 1
    #print(mod)
    
    hq = [[], [], []]
    for i in range(3):
        for y in range(C):
            diff = 0
            for x in mod[i]: diff += D[x][y] * mod[i][x]
            heappush(hq[i], (diff, y))
    #print(hq)
    
    cand = [[], [], []]
    for i in range(3):
        for _ in range(3):
            diff, color = heappop(hq[i])
            cand[i].append((diff, color))
    #print(cand)
    ans = 10**18
    for p in cand[0]:
        for q in cand[1]:
            for r in cand[2]:
                if p[1] == q[1] or q[1] == r[1] or r[1] == p[1]: continue
                ans = min(ans, p[0] + q[0] + r[0])
    print(ans)


if __name__ == "__main__":
    main()
