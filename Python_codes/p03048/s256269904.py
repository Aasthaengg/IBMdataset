r,g,b,n = map(int,input().split())

res = 0
v = 0
for i in range(n//r+1):
    for j in range(n//g+1):
        v = n-(i*r+j*g)
        #print('r,g,b=',i,j,v)
        if 0 <= v and v % b == 0:
            res += 1
        if v<0:break
print(res)