import itertools

N = int(input())
A = [int(x) for x in input().split()]

reg = 10**12
Acum = list(itertools.accumulate(A))
for i in range(N):
    L = Acum[i]
    R = Acum[-1] - L
    tmp = abs(L-R)
    reg = min(reg, tmp)
print(reg)