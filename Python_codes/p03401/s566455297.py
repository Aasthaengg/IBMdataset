#traveling plan
n=int(input())
lists=list(map(int,input().split()))
a=[0 for i in range(n+2)]
for i in range(n):
    a[i+1]=lists[i]

sums=0
for i in range(1,n+2):
    sums+=abs(a[i]-a[i-1])

for i in range(n):
    c=0
    c+=sums
    c+=abs(a[i+2]-a[i])
    c-=abs(a[i+1]-a[i])
    c-=abs(a[i+2]-a[i+1])
    print(c)