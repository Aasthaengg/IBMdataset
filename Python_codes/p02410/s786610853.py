n, m = map(int, raw_input().split())
A = [[0 for i in range(m)] for j in range(n)]
b = [0 for i in range(m)]
ans = [0 for i in range(n)]

for i in range(n):
    temp = map(int, raw_input().split())
    for j in range(m):
        A[i][j] += temp[j]
for i in range(m):
    b[i] = int(raw_input())
    
for i in range(n):
    for j in range(m):
        ans[i] += A[i][j]*b[j]
        
for i in range(n):
    print ans[i]