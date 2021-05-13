n, m = map(int, raw_input().split())

Matrix = [[0 for j in range(m)]for i in range(n)]
Vector = [0 for i in range(m)]
Ans = [0 for i in range(n)]

for i in range(n):
    M_element = map(int, raw_input().split())
    for j in range(m):
        Matrix[i][j] = M_element[j]

for i in range(m):
    Vector[i] = int(raw_input())

for i in range(n):
    for j in range(m):
        Ans[i] += Matrix[i][j] * Vector[j] 
for i in range(n):
    print Ans[i]