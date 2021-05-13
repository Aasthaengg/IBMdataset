n=int(input())

ans=[0]*(n+1)
r=int(n**0.5)+1

for x in range(1,r):
    for y in range(1,r):
        for z in range(1,r):
            t=x**2+y**2+z**2+x*y+y*z+z*x
            if t <= n:
                ans[t]+=1

for i in ans[1:]:
    print(i)
