N,M = map(int,input().split())
a = [input() for _ in range(N)]
b = [input() for _ in range(M)]

for i in range(N-M+1):
    for j in range(N-M+1):
        result = True
        for k in range(M):
            for l in range(M):
                if b[k][l] != a[i+k][j+l]:
                    result = False
        if result:
            print('Yes')
            exit()
print('No')