from statistics import median_high
n=int(input())
a=list(map(int,input().split()))
b=[]
for i in range(n):
    b.append(a[i]-i-1)
b.sort()
d=median_high(b)
ans=0
for i in range(n):
    ans+=abs(b[i]-d)
print(ans)