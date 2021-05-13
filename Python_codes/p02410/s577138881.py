n,m=map(int,input().split())
A =[[int(i) for i in input().split()] for j in range(n)]
b = []
for i in range(m):
    b.append(int(input()))
ans = [0 for i in range(n)]
for i in range(n):
    for j in range(m):
        ans[i] += A[i][j]*b[j]
for i in ans:
    print(i)