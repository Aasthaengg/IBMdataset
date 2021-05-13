import math
N,K = map(int,input().split())
P = max((N-K+1)/N,0)
cnt = 0
for k in range(1,min(N,K-1)+1):
    cnt += 2**(-math.ceil(math.log2(K/k)))
cnt = cnt/N
P += cnt
print(P)