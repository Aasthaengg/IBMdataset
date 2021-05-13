n,m = map(int,input().split())
a = [0]*n
for i in range(n):
    a[i] = list(input())
b = [0]*n
for i in range(m):
    b[i] = list(input())
ans = 0
for i in range(0,n-m+1):
    if ans == 1:
        break
    for j in range(0,n-m+1):
        sw = 1
        for x in range(m):
            for y in range(m):
                if a[i+x][j+y] == b[x][y]:
                    pass
                else:
                    sw = 0
        if sw == 1:
            ans = 1
            break
print(["No","Yes"][ans])