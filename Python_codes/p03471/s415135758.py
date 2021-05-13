n,y=map(int,input().split())
y //=1000
for i in range(n+1):
    for j in range(n-i+1):
        if n -(i+j) < 0:
            break
        if 9*i+4*j+n == y:
            print(i,j,n-(i+j))
            exit()
print('-1','-1','-1')