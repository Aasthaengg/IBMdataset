from collections import defaultdict

def diverta192_b():
    N = int(input())
    P = [tuple(map(int, input().split())) for _ in range(N)]
    if len(P) == 1:
        print(1)
        return
    dcnt = defaultdict(int)
    for i in range(N):
        xi, yi = P[i]
        for j in range(i):
            xj, yj = P[j]
            dx1, dy1 = xi-xj, yi-yj
            dx2, dy2 = xj-xi, yj-yi
            dcnt[(dx1,dy1)] += 1
            dcnt[(dx2,dy2)] += 1
    most = sorted(dcnt.values(), reverse=True)[0]
    ans = N - most
    print(ans)

diverta192_b()