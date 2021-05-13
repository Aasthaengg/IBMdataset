n,x=map(int,input().split())
a=list(map(int,input().split()))
b=0
a.sort()
for i in range(0,n):
    x-=a[i]
    b+=1
    if x<=0:
        break
    
if x==0:
    print(b)
else:
    print(b-1)