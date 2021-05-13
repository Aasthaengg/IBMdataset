n, m = list(map(int, input().split(" ")))
A = [[0 for _ in range(m)] for _ in range(n)]
b = [0 for _ in range(m)]

for i in range(n):
    A_line = list(map(int, input().split(" ")))
    for j, a in enumerate(A_line):
        A[i][j] += a
        
for j in range(m):
    b[j] = int(input())
    
for i in range(n):
    ans = 0
    for j in range(m):
        ans += A[i][j] * b[j]
    print (ans)