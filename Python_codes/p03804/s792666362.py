n,m = map(int,input().split())
a=[input() for _ in range(n)]
b=[input() for _ in range(m)]
for i in range(n-m+1):
    for j in range(n-m+1):
        flag=1
        for k in range(m):
            for l in range(m):
                if b[k][l]!=a[i+k][j+l]:
                    flag=0
                    break
            if not flag: break
        if flag:
            print("Yes")
            break
    if flag: break
if not flag: print("No")