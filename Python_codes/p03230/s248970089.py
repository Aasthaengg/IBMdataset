n = int(input())
m = int((n*2)**0.5)
if m*(m+1)!=n*2:
    print('No')
else:
    print('Yes')
    print(m+1)
    ans = [[0]*m for _ in range(m+1)]
    for i in range(m+1):
        for j in range(m):
            if i==0 and j==0:
                ans[i][j] = 1
            elif i==j:
                ans[i][j] = ans[i-1][j-1] + m-i + 1
            else:
                if i>j:
                    if i==j+1:
                        ans[i][j] = ans[i-1][j]
                    else:
                        ans[i][j] = ans[i-1][j] + 1
                else:
                    ans[i][j] = ans[i][j-1] + 1
    for a in ans:
        print(len(a), *a)