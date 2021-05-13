from heapq import heappush, heappop


def solve():
    N, H = map(int, input().split())
    cut_dmgs = []
    thr_dmgs = []
    for _ in range(N):
        a, b = list(map(int, input().split()))
        heappush(cut_dmgs, -a)
        heappush(thr_dmgs, -b)

    ans = 0
    max_cut_dmg = -min(cut_dmgs)
    while thr_dmgs:
        thr_dmg = -heappop(thr_dmgs) 
        if thr_dmg <= max_cut_dmg:
            break
        ans += 1
        H -= thr_dmg
        if H <= 0:
            return ans
    return ans + (H + max_cut_dmg - 1) // max_cut_dmg


print(solve())
