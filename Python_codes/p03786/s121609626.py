n=int(input())
a=list(map(int,input().split()))
a.sort()
ans=1
num=0
for i in range(n-1):
    num+=a[i]
    if num*2<a[i+1]:
        ans=i+2
print(n-ans+1)
