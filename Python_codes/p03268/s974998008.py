N, K = map(int, input().split())


cc = N//K
res = cc*cc*cc
if K%2 == 0 and N>=K/2:
    cc = (N-K/2)//K+1
    res+= cc*cc*cc

print(int(res))