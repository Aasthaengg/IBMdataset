import sys
import copy

N = int(input())
A = list(list(map(int, input().split())) for _ in range(N))

def fnc(M):
    m = list([True]*len(M) for _ in range(len(M)))
    for k in range(len(M)):
        for i in range(len(M)):
            for j in range(len(M)):
                if M[i][j] > M[i][k]+M[k][j]:
                    print(-1)
                    sys.exit()
                if M[i][j] == M[i][k]+M[k][j] and i != k and j != k:
                    m[i][j] = False
    return M,m

M,m = fnc(A)

ans = 0
for i in range(N):
    for j in range(N):
        if m[i][j]:
            ans += M[i][j]
        
print(ans//2)