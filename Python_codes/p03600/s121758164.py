N = int(input())
A = list(list(map(int,input().split()))for i in range(N))
B = [A[i][:] for i in range(N)]
ans = 0
for i in range(N):
    for j in range(i+1,N):
        flag = True
        for k in range(N):
            if not i != k != j:
                continue
            if A[i][j] == A[i][k] + A[j][k]:
                flag = False
            elif A[i][j] > A[i][k] + A[j][k]:
                print(-1)
                exit()
        if flag:
            ans += A[i][j]
print(ans)
