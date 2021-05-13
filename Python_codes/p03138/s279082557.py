N, K = map(int, input().split())
A = list(map(int, input().split()))
res = 0

# dより上位の桁については、XはKと一致
# d桁目についてはXは0で、Kは1である
# dより下位の桁については、Xはなんでもいい

# d = -1 は X = K の場合
for d in range(60, -2, -1):
    # Kが0の場合はダメ

    # ex.
    # 3 7
    # 1 6 3
    # の場合、d = 60, 59, ..., 3は除外される

    # K = 7 = 111(2)
    # d = 2の時、0**
    # d = 1の時、10*
    # d = 0の時、110
    # d = -1の時、111

    if d != -1 and (K & 1 << d) == 0:
        continue

    tmp = 0
    for e in range(60, -1, -1):
        mask = 1 << e

        # 今考えている桁について、bitが立っているAの要素の個数
        num = 0
        for i in range(N):
            if A[i] & mask:
                num += 1

        # XがKと一致している領域
        if e > d:
            # Kのbitが立っている場合
            # 反転が起こり、0の数(N-num)の分が足される
            if K & mask:
                tmp += mask * (N - num)
            # Kのbitが立っていない場合
            # bitの反転は起きない、1の数(num)の分が足される
            else:
                tmp += mask * num
        # この時、Xのbitは立っておらず、反転は起きない
        # 1の数(num)の分を足す
        elif e == d:
            tmp += mask * num
        # Xのbitは0と1の好きな方を取ることが出来る
        else:
            tmp += mask * max(num, N - num)
    res = max(res, tmp)

print(res)
