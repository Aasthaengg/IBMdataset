n, m = map(int, input().split())
a = [input() for i in range(n)]
b = [input() for i in range(m)]

for x in range(n-m+1):
    for y in range(n-m+1):
        for i in range(m):
            if b[i] != a[y+i][x:x+m]:
                break
        else:
            print('Yes')
            exit()
print('No')