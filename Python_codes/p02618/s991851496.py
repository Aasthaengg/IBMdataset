from time import time
import random
from collections import Counter


def main():
    random.seed(0)

    start = time()

    MAX = 26

    # 入力
    d = int(input())
    c = list(map(int, input().split()))
    s = [list(map(int, input().split())) for _ in range(d)]

    # 初期解を貪欲法で求める
    t = []
    prev = [0] * MAX
    for day, row in enumerate(s, 1):
        mxi = 1
        mx = 0
        for i, (es, ec) in enumerate(zip(row, c), 1):
            point = es + ec * (day - prev[i - 1])
            if point > mx:
                mx = point
                mxi = i

        prev[mxi - 1] = day
        t.append(mxi)

    # 初期解に対する満足度を計算
    last = [0] * MAX
    score = 0
    for day, e in enumerate(t, 1):
        score += s[day-1][e-1]
        last[e-1] = day

        for ec, elast in zip(c, last):
            score -= ec * (day - elast)

    # 変更を検討する日にちの選ばれやすさ
    d_li = []
    for i in range(1, d + 1):
        ln = max(1, (-(i - d // 2) ** 2 + d ** 2 // 4) // 500)
        d_li += [i] * ln

    di_max = len(d_li) - 1

    # 各日にちにおいて変更を検討するコンテストの選ばれやすさ
    sc = []
    for row in s:
        app = []
        for i, (es, ec) in enumerate(zip(row, c), 1):
            app += [i] * max(1, (es + ec * d) // 20)

        sc.append(app)

    # 時間の許す限り更新を検討する
    #cnt = 0
    #no_change = 0
    #counter = Counter()
    while time() - start <= 1.85:
        #cnt += 1
        prev_score = score

        di = random.randint(0, di_max)
        ed = d_li[di]
        qi = random.randint(0, len(sc[ed-1]) - 1)
        eq = sc[ed-1][qi]

        q_old = t[ed-1]
        d_prev = {q_old: 0, eq: 0}

        c_old = c[q_old-1]
        c_new = c[eq-1]

        for day, e in enumerate(t, 1):
            if e in d_prev.keys():
                d_prev[e] = day

            score += c_old * (day - d_prev[q_old])
            score += c_new * (day - d_prev[eq])

        score -= s[ed-1][q_old-1]
        score += s[ed-1][eq-1]

        t[ed-1] = eq

        d_prev = {q_old: 0, eq: 0}

        for day, e in enumerate(t, 1):
            if e in d_prev.keys():
                d_prev[e] = day

            score -= c_old * (day - d_prev[q_old])
            score -= c_new * (day - d_prev[eq])

        if prev_score > score:
            val = (score - prev_score) / (1000 * (time() - start))
            #print(time() - start, val)
            if val > -10:
                continue
            #counter[int(val)] += 1
            #no_change += 1
            t[ed-1] = q_old
            score = prev_score

    print(*t, sep="\n")
    #print("#############")
    #print("cnt", cnt)
    #print("no change", no_change)
    #print(sorted(counter.items()))


if __name__ == "__main__":
    main()
