def calc_median(X):
    #中央値計算
    Xl = len(X)
    if Xl % 2:
        ret = X[(Xl + 1) // 2 - 1]
    else:
        ret = (X[Xl // 2 - 1] + X[Xl // 2]) / 2

    return ret


N = int(input())
AB = [list(map(int, input().split())) for _ in range(N)]

A = [AB[i][0] for i in range(N)]
B = [AB[i][1] for i in range(N)]

A.sort()
B.sort()

AM = calc_median(A)
BM = calc_median(B)

if N % 2:
    ans = BM - AM + 1
else:
    ans = int((BM - AM) * 2 + 1)

print(ans)
