f=[0,1,1,2,3,5,8,13,21,34,55,89];h,w,k=map(int,input().split());a=[0]*(w+2);a[1]=1
for i in range(h):a=[0]+[(f[j-1]*f[w-j+1]*a[j-1]+f[j]*f[w-j+1]*a[j]+f[j]*f[w-j]*a[j+1])%(10**9+7)for j in range(1,w+1)]+[0]
print(a[k])