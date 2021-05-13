N,M = map(int,input().split())

A = [input() for _ in range(N)]
B = [input() for _ in range(M)]

ans = 0
for i in range(N-M+1):
    for h in range(N-M+1):
        cnt = 0
        for k in range(M):
            for j in range(M):
                if A[i+k][h+j] != B[k][j]:
                    cnt += 1
        if cnt == 0:
            ans += 1
if ans != 0:
    print("Yes")
else:
    print("No")