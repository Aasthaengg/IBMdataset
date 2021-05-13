n,m = map(int,input().split())
cake = []

for i in range(n):
    x,y,z = map(int,input().split())
    cake.append([x,y,z])
ans = 0
    
for i in range(2):
    for j in range(2):
        for k in range(2):
            cakesum = []
            ansk = 0
            
            for xx,yy,zz in cake:
                a = xx * ((-1)**i) + yy * ((-1)**j) + zz * ((-1)**k)
                cakesum.append(a)
                
            cakesum.sort(reverse = True)
            ansk = sum(cakesum[:m])
            
            ans = max(ansk,ans)
            
print(ans)