n,x=map(int,input().split())
a=sorted(list(map(int,input().split())))
count=0
for i in range(n):
    if i==n-1:
        if x==a[i]:
            count+=1
        break
    if x<a[i]:
        break
    x-=a[i]
    count+=1
print(count)