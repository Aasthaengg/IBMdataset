N,M,*f = open(0).read().split()
N = int(N)
M = int(M)
A = f[:N]
B = f[N:]
for i in range(N-M+1):
    for j in range(N-M+1):
        if A[i][j:j+M] == B[0]:
            for k in range(1,M):
                if A[i+k][j:j+M] != B[k]:
                    break
            else:
                print('Yes')
                break
    else:
        continue
    break
else:
    print('No')