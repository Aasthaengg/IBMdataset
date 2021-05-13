n=int(input())
a=[]
for i in range(n):
    a.append(int(input()))
maxv=a[1]-a[0]
minv=a[0]
for j in range(1,n):
    maxv=max(maxv,a[j]-minv)
    minv=min(minv,a[j])
print(maxv)
    
