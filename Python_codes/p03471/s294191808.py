n,y = map(int,input().split())

for i in range(y // 10000 + 1):
    for j in range(y // 5000 + 1):
        k = n - i - j
        if 0 <= k and 10000 * i + 5000 * j + 1000 * k == y:
            print(i,j,k,sep=" ")
            exit()
print("-1 " + "-1" + " -1")