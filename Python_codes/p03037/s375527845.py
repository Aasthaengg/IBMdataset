N, M = map(int, input().split())
LR = [list(map(int, input().split())) for i in range(M)]
Lmax = max([lr[0] for lr in LR])
Rmin = min([lr[1] for lr in LR])
if Rmin >= Lmax:
    print(Rmin - Lmax + 1)
else:
    print(0)
