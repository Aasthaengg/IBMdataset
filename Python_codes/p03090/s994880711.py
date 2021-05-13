n = int(input())

path = [[True for i in range(n)] for i in range(n)]

if n%2 == 0:
    for i in range(n//2):
        path[i][i] = False
        path[i][n-i-1] = False
        path[n - i - 1][i] = False
else:
    for i in range(n//2):
        path[i][i] = False
        path[i][n-i-2] = False
        path[n - i - 1][i] = False

ans = []
# print(path)

for i in range(n):
    for j in range(i+1,n):
        if path[i][j]:
            ans.append([i+1,j+1])

print(len(ans))
for a in ans:
    print(str(a[0])+" "+str(a[1]))