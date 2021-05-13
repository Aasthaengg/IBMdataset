N,K=map(int,input().split())
def kosuu(n,b,k):
    res = 0
    res += n//b * (b-k)
    diff = n%b - k
    if diff >= 0:
        res += diff + 1
    return res

cnt = 0
for b in range(K+1,N+1):
    ko = kosuu(N,b,K)
    # print(b,ko)
    cnt += ko

if K == 0:
    cnt -= N

print(cnt)