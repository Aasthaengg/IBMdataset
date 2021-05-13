
N,K = map(int,input().split())

ans = 0
for b in range(K+1,N+1):
    tmp = 0
    multi = int(N/b)
    tmp += (b-K) * multi
    if K==0:
        tmp += max(0,N%b)
    else:
        tmp += max(0,(N%b-K+1))
    ans += tmp
print(ans)