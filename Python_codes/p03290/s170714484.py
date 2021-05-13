D, G = map(int, input().split())
p = []
c = []
for _ in range(D):
    pi, ci = map(int, input().split())
    p.append(pi)
    c.append(ci)

res = 10**9
# どの問題を全完するか決め打つ
for bit in range(1 << D):
    sum = 0
    num = 0

    # bitが立っている = 全完する問題について
    for i in range(D):
        if bit & (1 << i):
            sum += c[i] + p[i] * 100 * (i + 1)
            num += p[i]

    # 既にGを超えていたら「中途半端に」解く必要はない
    if sum >= G:
        res = min(res, num)

    # 「中途半端に」解く必要がある場合
    else:
        # どの問題を「中途半端に」解くか
        # 全完していない問題のうち、最も点数が高いもの
        # 全て全完している場合に注意
        d = -1
        for i in range(D - 1, -1, -1):
            if not(bit & (1 << i)):
                d = i
                break
        if d == -1:
            continue
        else:
            # 全完１歩手前まで順に試す
            for j in range(p[d] - 1):
                sum += 100 * (d + 1)
                num += 1
                if sum >= G:
                    break
            # p-1問解いてもGに達していない場合に注意
            if sum >= G:
                res = min(res, num)

print(res)
