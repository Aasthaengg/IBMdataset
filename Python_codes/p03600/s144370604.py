N = int(input())
A = []
for _ in range(N):
    A.append(list(map(int, input().split())))

ans = 0

for i in range(N):
    for j in range(N):
        used = True
        for k in range(N):
            if i == k or j == k:
                continue
            tmp = A[i][k] + A[k][j]
            if A[i][j] > tmp:
                print(-1)
                exit()
            if A[i][j] == tmp:
                used = False
        if used:
            ans += A[i][j]
print(ans//2)
