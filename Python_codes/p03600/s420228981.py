n = int(input())
a = [list(map(int,input().split())) for i in range(n)]

total = 0
for i in range(n-1):
    for j in range(i+1,n):
        flg = True
        for x in range(n):
            if x == i or x == j:
                continue
            if a[i][j] > a[i][x] + a[j][x]:
                print(-1)
                exit()
            elif a[i][j] == a[i][x] + a[j][x]:
                flg = False
                break
        if flg:
            total += a[i][j]
            
print(total)