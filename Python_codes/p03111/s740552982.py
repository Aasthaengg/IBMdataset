
N,A,B,C = map(int, input().split())
bamboos = [int(input()) for _ in range(N)]
#print("---", bamboos)
INF = float("inf")
ans = INF
def solve(idx, cnt_merge, a, b, c):

    if idx == N:
        if min(a,b,c) > 0:
            return abs(A - a) + abs(B - b) + abs(C - c) + 10 * (cnt_merge-3)
        else:
            return INF

    pa = solve(idx+1, cnt_merge+1, a+bamboos[idx], b, c)
    pb = solve(idx+1, cnt_merge+1, a, b+bamboos[idx], c)
    pc = solve(idx+1, cnt_merge+1, a, b, c+bamboos[idx])
    pn = solve(idx+1, cnt_merge, a, b, c)
    return min(pa, pb, pc, pn)


print(solve(0,0,0,0,0))