# -*- coding:utf-8 -*-

def solve():
    MOD = 2019
    S = input()

    """解説AC"""
    # A列を作成
    As = []
    d = 1
    for moji in S[::-1]:
        a = (int(moji)*d)%MOD
        As.append(a)
        d = (d*10)%MOD

    # 累積和を作成
    ruiseki = [0]
    for i, a in enumerate(As):
        r = (ruiseki[i] + a)%MOD
        ruiseki.append(r)

    # ruiseki[i] ≡ ruiseki[j] (mod 2019) となる総数を数える
    ruiseki_dic = {}  # combinationの計算でもいける
    ans = 0
    for r in ruiseki:
        if not r in ruiseki_dic:
            ruiseki_dic[r] = 1
        else:
            ans += ruiseki_dic[r]
            ruiseki_dic[r] += 1

    print(ans)



if __name__ == "__main__":
    solve()
