x=int(input())
r=10**9 
l=0
while r-l>1:
    mid=(r+l)//2 
    if x<=mid*(mid+1)//2:
        r=mid
    else:
        l=mid

print(r)  