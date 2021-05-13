ans=0 
n,a,b=map(int,input().split())
l=[int(i) for i in input().split()]
for i in range(1,n):
    d=l[i]-l[i-1]
    c1= d*a 
    c2=b 
    ans+=min(c1,c2)
print(ans)