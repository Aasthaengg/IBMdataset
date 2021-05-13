n, m = map(int, input().split())
lights = [list(map(int, input().split()))[1:] for i in range(m)]
P = list(map(int, input().split()))

res = 0
# bit列の組み合わせについて
for bit in range(1 << n):
    ok = True
    # 各電球について
    for i in range(m):
        # 電球iのonの状態のスイッチの個数
        cnt = 0
        # 電球の各スイッチについて
        for v in lights[i]:
            v -= 1
            # 電球のスイッチがvのon/off判定
            if bit & (1 << v):
                cnt += 1
        # 電球iは点灯しているか判定
        if cnt % 2 != P[i]:
            ok = False
    if ok:
        res += 1
print(res)