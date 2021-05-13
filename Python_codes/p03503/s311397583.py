N = int(input())
 
F = []
 
for _ in range(N):
    f = list(input().strip().split())
    F.append(int("".join(f), 2))

P = [list(map(int, input().split())) for _ in range(N)]

ans = -10**10-7

for i in range(1,2**10):
    candi = 0
    for j in range(N):
        tmp = i & F[j]
        p = format(tmp, 'b').count("1")
        candi += P[j][p]
    ans = max(ans,candi) 
    
print(ans)