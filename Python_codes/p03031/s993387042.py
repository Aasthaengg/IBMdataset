N,M = map(int,input().split())
light = [list(map(int,input().split())) for _ in range(M)]
p = list(map(int,input().split()))

cnt = 0
for i in range(2**N):
    b = [0]*N
    for j in range(N):
        if ((i >> j) & 1):
            b[j] = 1
    
    for k in range(M):
        num = 0
        for l in range(len(light[k])-1):
            num += b[light[k][l+1]-1] 
        if num%2 != p[k]:
            break
    else: cnt += 1
print(cnt)