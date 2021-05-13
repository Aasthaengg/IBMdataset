import math
N,K=map(int,input().split())
pro=0
if N==1 and K==1:
    print(1)
elif N>=K:
    pro+=(N-K+1)/N
    for k in range(1, K):
        r = math.ceil(math.log(K / k,2))
        pro += 0.5**r / N
    print(pro)

else:
    for k in range(1, N+1):
        r = math.ceil(math.log(K / k,2))
        pro += 0.5**r / N
    print(pro)

