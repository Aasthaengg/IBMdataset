n = int(input())
a = [2,1,3]
for i in range(n):
  a[0]=a[1]
  a[1]=a[2]
  a[2]=a[0]+a[1]
print(a[0])