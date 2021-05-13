import sys
def input(): return sys.stdin.readline().strip()
def mapint(): return map(int, input().split())
sys.setrecursionlimit(10**9)

N, M = mapint()
AB = [list(mapint()) for _ in range(N)]
CD = [list(mapint()) for _ in range(M)]

for a, b in AB:
    dist = 10**18
    ans = -1
    for i in range(M):
        c, d = CD[i]
        if abs(a-c)+abs(b-d)<dist:
            ans = i+1
            dist = abs(a-c)+abs(b-d)
    print(ans)