n,m = map(int, input().split())
a = [str(input()) for i in range(n)]
b = [str(input()) for i in range(m)]
for i in range(0,n-m+1):
    for j in range(0,n-m+1):
        ans = 1
        for k in range(0,m):
            for l in range(0,m):
                if a[i+k][j+l] != b[k][l]:
                    ans = 0
                    break
        if ans == 1:
            print('Yes')
            exit()
print('No')
