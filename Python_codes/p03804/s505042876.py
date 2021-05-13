n,m=map(int,input().split())
a=[]
b=[]
for i in range(n):
    a.append(list(input()))
for i in range(m):
    b.append(list(input()))
for i in range(n-m+1):
    for j in range(n-m+1):
        flg=True
        for k in range(m):
            for kk in range(m):
                if b[k][kk]!=a[i+k][j+kk]:
                    flg=False
        if flg:
            print("Yes")
            exit()
print("No")