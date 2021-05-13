n,a,b=int(input()),[],[]
m=n+(n%2==0)
for i in range(1,n):
  for j in range(i+1,n+1):
    if i+j!=m:a.append(i);b.append(j)
l=len(a)
print(l)
for i in range(l):print(a[i],b[i])
