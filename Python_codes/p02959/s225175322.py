n=int(input())
l=list(map(int,input().split()))
d=list(map(int,input().split()))
s=0
for i in range(n):
    if(l[i]>=d[i]):
        s+=d[i]
    else:
        s+=min(l[i]+l[i+1],d[i])
        l[i+1]=max(0,l[i+1]-(d[i]-l[i]))
print(s)
