N,K = map(int,input().split())

ans = 0
for i in range(1,N+1):
    tmp = 1/N
    now = i
    while now < K:
        now *= 2
        tmp /= 2
    
    ans += tmp

print(ans)