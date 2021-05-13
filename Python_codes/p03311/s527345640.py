from statistics import median
n=int(input())
a=list(map(int,input().split()))
mid=0
l=[]
for i in range(n):
    l+=[a[i]-i-1]

mid=median(l) if n%2!=0 else sorted(l)[n//2]
ans=0
for i in range(n):
    ans+=abs(a[i]-(mid+i+1))

print(int(ans))
