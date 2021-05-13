n=int(input())
ans=[0]*(n+1)
m=int(n**0.5)+1
for x in range(1,m):
    for y in range(1,m):
        for z in range(1,m):
            a=x**2+y**2+z**2+x*y+y*z+z*x
            if 1<=a<=n:
                ans[a]+=1
for i in range(1,n+1):
    print(ans[i])