l,r=map(int,input().split())
x=l//2019
y=l%2019
z=r//2019
w=r%2019
if x<z:
    print(0)
else:
    if y==0:
        print(0)
    else:
        ans=2020
        for i in range(y,w):
            for j in range(i+1,w+1):
                ans=min(ans,(i*j)%2019)
        print(ans)
