N,M = map(int,input().split())

A = [input() for i in range(N)]
B = [input() for i in range(M)]


for i in range(N-M+1):
    for j in range(N-M+1):
        flg = True
        for k in range(M):
            for l in range(M):
                if A[i+k][j+l] == B[k][l]:
                    pass
                else:
                    flg=False
                    break
            if flg==False:
                break

        if flg:
            break
    if flg:
        break
if flg:
    print('Yes')
else:
    print('No')