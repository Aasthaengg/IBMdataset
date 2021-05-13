n=int(input())
a=list(map(int,input().split()))
m=1000
s=0
for i in range(n-1):
  if a[i]<a[i+1]:
    s+=m//a[i]
    m=m%a[i]
  else:
    m+=s*a[i]
    s=0
print(m+a[n-1]*s)