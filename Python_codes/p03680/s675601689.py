n=int(input())
a=[0]*n
for i in range(n):
    a[i]=int(input())
f=1
count=0
while f!=2 and count<n+2:
    f=a[f-1]
    count=count+1
if count>n:
    count=-1
print(count)
