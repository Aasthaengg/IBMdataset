a=list(map(int,input().split()))
for i in range(a[2]):
    if a[i%2]%2==1:
        a[i%2]-=1
    res=a[i%2]//2
    a[i%2]-=res
    a[(i+1)%2]+=res
print(a[0],a[1])