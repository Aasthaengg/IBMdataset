n = int(input())
p = list(map(float,input().split()))
a = [[0 for i in range(n+1)] for j in range(n+1)]
a[0][0] = 1
for i in range(1, n+1):
    for j in range(n+1):
        if j == 0:
            a[i][j] = (1-p[i-1])*a[i-1][j]
        elif(i<j):
            a[i][j] = 0
        else:
            a[i][j] = p[i-1]*(a[i-1][j-1])
            if i-1>=j:
                a[i][j] += (1-p[i-1])*a[i-1][j]
mh = (n+1)//2
ans = 0 
for i in range(mh, n+1):
    ans += a[n][i]
print(ans)