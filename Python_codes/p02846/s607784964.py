def main(v1, v2, t1, t2):
    if v1 * v2 >= 0:  # どんどん離れる
        return 0
    # v1>0, v2<0とする
    d1 = abs(v1) * t1
    d2 = abs(v2) * t2

    if d1 > d2:  # 追いつけない
        return 0
    if d1 == d2:  # 毎回ちょうど追いつく
        return "infinity"

    dL = d2 - d1
    peak = (d1 + dL - 1) // dL
    if d1 % dL == 0:
        return peak * 2
    else:
        return peak * 2 - 1


t1, t2 = map(int, input().split())
a1, a2 = map(int, input().split())
b1, b2 = map(int, input().split())
print(main(a1-b1, a2-b2, t1, t2))