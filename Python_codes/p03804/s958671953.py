N,M = map(int,input().split())
A = [input() for _ in range(N)]
B = [input() for _ in range(M)]
#ans = False
for dx in range(N-M+1):
    for dy in range(N-M+1):
        flg = True
        for i in range(M):
            for j in range(M):
                if A[i+dx][j+dy] != B[i][j]:
                    flg = False
        if flg:
            print("Yes")
            exit()
print("No")