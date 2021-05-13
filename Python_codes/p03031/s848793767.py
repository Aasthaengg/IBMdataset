N,M = list(map(int,input().split()))
ks =  [list(map(int,input().split())) for _ in range(M)]
p = list(map(int,input().split()))

Nlen = 2**N
ans = 0

for i in range(Nlen):
    total = 0
    for j in range(M):
        count = 0
        for k in range(1,ks[j][0]+1): 
            if i & 2**(ks[j][k]-1) == 2**(ks[j][k]-1):
                count += 1
        if count % 2 == p[j]:
            total += 1
    if total == M:
        ans += 1

print(ans)