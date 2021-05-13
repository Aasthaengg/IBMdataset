
N, K = map(int,input().split())
ans = 0

for i in range(1,N+1):
    
    c = 1
    p = 1/N
    while c*i<K:
        c *= 2
        p /= 2
    ans += p
print(ans)