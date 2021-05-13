n=int(input())
a=list(map(int,input().split()))
a.sort()
d=[0]*n
d[0]=1
s=[0]*n
s[0]=a[0]

for i in range(1,n):
  s[i]=s[i-1]+a[i]
for i in range(1,n):
    if a[i]>2*s[i-1]:
        d[i]=1
    else:
        d[i]=d[i-1]+1
print(d[n-1])