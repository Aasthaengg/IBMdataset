N = int(input())

A = [[0]*N for i in range(N)]

for i in range(N):
    A[i] = list(map(int,input().split()))
B = [[A[i][j] for j in range(i+1,N)] for i in range(N-1)]
#print(A)
#print(B)

det = 0

for i in range(N-1):
    for j in range(i+1,N):
        for k in range(N):
            if A[i][j] > A[i][k] + A[k][j]:
                det = -1
                break
            elif i != k and j != k and A[i][j] == A[i][k] + A[k][j]:
                B[i][j-(i+1)] = 0
                #print(i,j,k,B)
        
        if det == -1:
            break

    if det == -1:
        break

if det == 0:
    ans = 0
    for i in range(N-1):
        for j in range(i+1,N):
            ans += B[i][j-(i+1)]
else:
    ans = -1

print(ans)
