from decimal import Decimal, getcontext
getcontext().prec = 20
N, K = map(int, input().split())
res = 0
for p in range(1,N+1):
    cnt = 0
    q = 1
    while p*q <K:
        cnt += 1
        q *= 2
    res += Decimal(pow(1/2,cnt))
print(res/N)