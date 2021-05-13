n,y = map(int,input().split())
for i in range(n+1):
    for j in range(n+1-i):
        k = n - i - j
        if i*10000 + j*5000 + k*1000 == y and  i + j + k == n and k >= 0:
            print(i,j,k)
            exit()
print("-1 -1 -1")
