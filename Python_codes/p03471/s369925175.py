n,y = map(int, input().split())
a,b,c = -1,-1,-1
for i in range(n+1):
    for j in range(n+1):
        total = 10000*i + 5000*j + 1000*(n-i-j)
        if(total == y and (n-i-j)>=0):
            a,b,c = i,j,(n-i-j)
print(a,b,c)
