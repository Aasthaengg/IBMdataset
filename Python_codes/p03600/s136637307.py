N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]
ans = 0

for i in range(N):    
    for j in range(N):
        ok = True
        for k in range(N):
            if A[i][j] > A[i][k] + A[k][j]:
                print(-1)
                exit()
            if i != k and j != k:
                if A[i][j] == A[i][k] + A[k][j]:
                    ok = False
        if ok:
            ans += A[i][j]

print(ans//2)
