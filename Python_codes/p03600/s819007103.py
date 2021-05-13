import copy

n = int(input())
A = []
for _ in range(n):
    a = list(map(int, input().split()))
    A.append(a)

Check = copy.deepcopy(A)

for k in range(n):
    for i in range(n):
        for j in range(n):
            Check[i][j] = min(Check[i][j], Check[i][k]+Check[k][j])

Graph_exist = True
for i in range(n):
    for j in range(n):
        if A[i][j] != Check[i][j]:
            Graph_exist = False

Road_exist = [[True for _ in range(n)] for _ in range(n)]
for i in range(n):
    Road_exist[i][i] = False

for k in range(n):
    for i in range(n):
        for j in range(n):
            if i == j or i==k or j==k:
                continue
            if A[i][j] == (A[i][k] + A[k][j]):
                Road_exist[i][j] = False

ans = 0
for i in range(n):
    for j in range(i+1,n):
        if Road_exist[i][j] == True:
            ans += A[i][j]

if Graph_exist == False:
    ans = -1
print(ans)