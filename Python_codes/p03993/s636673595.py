n=int(input())
a=list(map(int,input().split()))
for i in range(n):
  a[i]=a[i]-1
c=0
for i in range(n):
  if a[a[i]]==i:
    c+=1
print(c//2)