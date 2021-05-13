N,M,C = map(int,input().split())
Bls = list(map(int,input().split()))
ii = 0
for i in range(N):
    sum1 = 0
    Als = list(map(int,input().split()))
    for j in range(M):
        sum1 += Bls[j]*Als[j]
    if sum1 + C > 0:
        ii += 1
print(ii)