n = int(input())
a=[]
b=[]
for i in range(n):
    h,m=list(map(int,input().split()))
    a.append(h)
    b.append(m)
a.sort()
b.sort()

if n%2:
    k=(n-1)//2
    
        
    print(b[k]-a[k]+1)
else:
    k=n//2
    

    
    print(b[k]+b[k-1]-(a[k]+a[k-1])+1)

