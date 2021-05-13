r,c = map(int,input().split())
table = [[0]*(c+1) for i in range(r+1)]

for i in range(r):
    table[i] = list(map(int,input().split()))
    table[i].append(sum(table[i]))
    for j in range(c+1):
        table[r][j] += table[i][j]

for i in range(r+1):
    for j in range(c+1):
        if(j == c):
            print("%d" %(table[i][j]),end="")
        else:
            print("%d " %(table[i][j]),end="")
    print()
