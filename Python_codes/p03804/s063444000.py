N, M = map(int, input().split())
A = [input() for _ in range(N)]
B = [input() for _ in range(M)]

for i in range(N-M+1):
    for j in range(N-M+1):
        ok = True
        for y in range(M):
            for x in range(M):
                if A[i+y][j+x] != B[y][x]:
                    ok = False
                    break
        if ok:
            print("Yes")
            exit()
print("No")