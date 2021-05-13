def calc_median(X):
    #中央値計算
    Xl = len(X)
    if Xl % 2:
        #ret = X[(Xl + 1) // 2 - 1]
        ret = X[Xl // 2]
    else:
        ret = (X[Xl // 2 - 1] + X[Xl // 2]) / 2

    return ret


N, *AB = map(int, open(0).read().split())

A = sorted(AB[::2])
B = sorted(AB[1::2])

AM = calc_median(A)
BM = calc_median(B)

if N % 2:
    ans = BM - AM + 1
else:
    ans = int((BM - AM) * 2 + 1)

print(ans)
