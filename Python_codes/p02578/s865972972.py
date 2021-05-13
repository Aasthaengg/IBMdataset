n=int(input())
a=[int(x) for x in input().split()]
b=a[0]
c=0
for i in range(1,n):
  if a[i]<b:
    c+=b-a[i]
  else:
    b=a[i]
print(c)