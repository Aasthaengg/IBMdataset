l,r=map(int,input().split())
m=2019
c=m-1
r=min(r,l+m-1)
for i in range(l,r):
    for j in range(i+1,r+1):
        s=i*j
        c=min(c,s%m)
print(c)
