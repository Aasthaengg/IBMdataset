import math
def li():
    return [int(x) for x in input().split()]

d, g = li()
ps, cs = [], []
for i in range(d):
    p, c = li()
    ps.append(p)
    cs.append(c)
ps.reverse()
cs.reverse()
# ボーナス得点のパターンを先に全て列挙し、点数が届いていなければ高得点から埋めていく
qcnts = []

for mask in range(2**d):
    score = 0
    qcnt = 0
    #ボーナス計算
    for i in range(d):
        # i番目のフラグが立ってる
        if mask & (1 << i):
            score += cs[i] + ps[i] * 100 * (d-i)
            qcnt += ps[i]
    #残りを高得点から埋めていく
    required_score = g - score
    if required_score >= 0:
        for i in range(d):
            # i番目のフラグが立っているならスキップ
            if mask & (1 << i):
                continue
            required_qcnt = min(math.floor(required_score / (100 * (d-i))), ps[i])
            qcnt += required_qcnt
            score += required_qcnt * (100 * (d-i))
            if score >= g:
                break
    qcnts.append(qcnt)

print(min(qcnts))
