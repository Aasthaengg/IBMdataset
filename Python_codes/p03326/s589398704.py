n, m = map(int, input().split())
L = [[0, 0, 0] for _ in range(n)]
for i in range(n):
    x, y, z = map(int, input().split())
    L[i][0], L[i][1], L[i][2] = x, y, z

ans = 0
for i in range(2**3):
    temp = [0]*n
    for k in range(n):
        for j in range(3):
            if (i >> j) & 1:
                temp[k] += L[k][j]
            else:
                temp[k] += L[k][j]*(-1)
    temp.sort(reverse=True)
    ans = max(ans, sum(temp[0:m]))
print(ans)    
