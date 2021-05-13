


N,K = map(int, input().split())
XY = [tuple(map(int, input().split())) for _ in range(N)]

"""
辺の上に点が乗っていても四角形の中に含まれると見なされるので、辺はいずれかの点の上を通るように引くと面積を小さくできる
各点のx,yをsetで持っておいて、全探索できるか？
→ N <= 50なので4つの辺の選び方が50**4、この範囲にK個以上入っているかでさらに *50なので間に合うか微妙？
小さい値で ^5 なので、間に合うかも
"""

LR = [] # left,right
TB = [] # top, bottom
for x,y in XY:
    LR.append(x)
    TB.append(y)


LR = list(set(LR))
LR.sort()
TB = list(set(TB))
TB.sort()


def more_than_K(l,r,t,b):
    cnt = 0
    for x,y in XY:
        if l <= x <= r and b <= y <= t:
            cnt += 1
    return cnt >= K

ans = float("inf")
for p in range(len(LR)):
    for q in range(p+1, len(LR)):
        for r in range(len(TB)):
            for s in range(r+1, len(TB)):

                if more_than_K(LR[p], LR[q], TB[s], TB[r]):
                    ans = min(ans, (LR[q] - LR[p]) * (TB[s] - TB[r]))


print(ans)
