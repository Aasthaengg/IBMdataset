from heapq import heappop as hpp, heappush as hp
import sys
N, Q = map(int, input().split())
stx = [tuple(map(int, sys.stdin.readline().split())) for _ in range(N)]
stx = [(s-x, t-x, x) for s, t, x in stx]
stx.sort(reverse = True)

D = [int(sys.stdin.readline()) for _ in range(Q)] 
H = []
ans = [None]*Q

for i, d in enumerate(D):
    while stx and stx[-1][0] <= d:
        hp(H, stx.pop()[1:][::-1])    
    while H and H[0][1] <= d:
        hpp(H)
    if not H:
        ans[i] = -1
    else:
        ans[i] = H[0][0]

for a in ans:
    print(a)