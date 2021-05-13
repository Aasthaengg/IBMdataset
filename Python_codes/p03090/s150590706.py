n=int(input())
a=[]
b=[]
m=n+(n%2==0)
for i in range(1,n):
  for j in range(i+1,n+1):
    if i+j!=m:a.append(i);b.append(j)
print(len(a))
for i,j in zip(a,b):print(i,j)