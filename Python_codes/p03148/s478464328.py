# -*- coding: utf-8 -*-
"""
D - Various Sushi
https://atcoder.jp/contests/abc116/tasks/abc116_d
AC
"""
import sys

from collections import Counter

def solve(N, K, sushi):
    sushi.sort(key=lambda x: x[1], reverse=True)
    pick = sushi[:K]            #  おいしさポイントの高い方からK個の寿司を選択
    pick_type = set([t for t, d in pick]) # 選択済の種類

    cnt = Counter()             #  各種類の寿司が何個ずつあるか覚えておく
    for t, d in pick:
        cnt[t] += 1

    rem = dict()                #  未選択の種類の寿司のうち、一番おいしさポイントが高い物
    for t, d in sushi:
        if t not in pick_type:
            rem[t] = max(rem.get(t, 0), d)
    res = sorted([[k, v] for k, v in rem.items()], key=lambda x: x[1]) # おいしさで昇順にソート(一番おいしい物が末尾)

    manzoku = sum([d for t, d in pick])
    ans = [manzoku + len(pick_type)**2] #  現在の選択でのスコア、ここから種類を1つずつ増加させていきスコアを計算する
    while len(pick_type) < K and pick and res:
        t, d = res.pop()
        pick_type.add(t)
        tt, dd = pick.pop()
        while cnt[tt] == 1 and pick:
            tt, dd = pick.pop()
        if cnt[tt] > 1:
            cnt[tt] -= 1
            manzoku = manzoku - dd + d
            ans.append(manzoku+ len(pick_type)**2)
    return max(ans)


def main(args):
    N, K = map(int, input().split())
    sushi = [[int(i) for i in input().split()] for _ in range(N)]
    ans = solve(N, K, sushi)
    print(ans)


if __name__ == '__main__':
    main(sys.argv[1:])
