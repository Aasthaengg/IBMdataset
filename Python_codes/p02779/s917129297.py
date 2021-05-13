n=int(input())
a=[]
a=[int(v) for v in input().split()]
a.sort()
dem=0
for i in range(0,n-1):
    if(a[i]==a[i+1]):
        dem+=1
if(dem==0):
    print("YES")
else:
    print("NO")