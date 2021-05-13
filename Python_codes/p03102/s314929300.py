N, M, C=(int(x) for x in input().split())
B = list(map(int, input().split()))
A = [([] for _ in range(M)) for _ in range(N)]
cou = 0

for i in range(N):
    A[i] = list(map(int, input().split()))

for i in range(N):
    ju=0
    for j in range(M):
        ju += A[i][j]* B[j]
    if (ju + C > 0):
        cou +=1

print(cou)