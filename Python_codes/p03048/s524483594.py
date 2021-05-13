r,g,b,n=map(int,input().split())
cnt=0
for i in range(int(n//r)+1):
    for j in range(int(n//g)+1):
        if (n-i*r-j*g) %b ==0 and 0<=(n-i*r-j*g) // b <= 3000:
            # print(i,j,(n-i*r-j*g)//3)
            cnt+=1
print(cnt)