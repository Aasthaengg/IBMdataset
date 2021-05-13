n,x= list(map(int, input().strip().split()))
a= list(map(int, input().strip().split()))
a.sort()
count=0
f=0
for i in range(n):
    count+=a[i]
    if count>x:
        f=i
        break
if count<x:
    print(n-1)
elif count==x:
    print(n)
else:
    print(f)