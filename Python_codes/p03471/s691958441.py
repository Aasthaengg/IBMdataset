k,s = map(int,input().split())
for i in range(k+1):
    for j in range(k+1-i):
        if 10000*i+5000*j+1000*(k-i-j) == s:
            print(i,j,k-i-j)
            exit()
print(-1,-1,-1)