n=int(input())
a=sorted([int(input()) for i in range(n)])
res=1
for i in range(1,n):
    if a[i-1]<a[i]:res+=1
print(res)