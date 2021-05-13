k,n=map(int,input().split())


a=list(map(int,input().split()))
max=0
a.sort()

for i in range(1,n):
    if max<abs(a[i]-a[i-1]):
        max=abs(a[i]-a[i-1])

if max<k-abs(a[0]-a[-1]):
    max=k-abs(a[0]-a[-1])

print(k-max)

