n,m = map(int,input().split())
a = [input() for i in range(n)]
b = [input() for i in range(m)]
ans = "No"
for i in range(n-m+1):
    for j in range(n-m+1):
        flag = True
        for k in range(m):
            if a[i+k][j:j+m]!=b[k]:
                flag = False
                break
        if flag:
            ans = "Yes"
            break
print(ans)