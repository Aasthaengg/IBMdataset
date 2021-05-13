N = int(input())
F = [list(map(int, input().split())) for _ in range(N)]
P = [list(map(int, input().split())) for _ in range(N)]
ans = -10**18

for i in range(1, 2**10):
    A = [0]*10
    
    for j in range(10):
        if (i>>j)&1:
            A[j] = 1
        
    ans_cand = 0
    
    for j in range(N):
        c = 0
        
        for k in range(10):
            if F[j][k]==1 and A[k]==1:
                c += 1
        
        ans_cand += P[j][c]
    
    ans = max(ans, ans_cand)

print(ans)