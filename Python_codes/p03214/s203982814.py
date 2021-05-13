n=int(input())
a=list(map(int,input().split()))
ave=sum(a)/n
x=0
m=10**9
for i in range(n):
    if abs(ave-a[i])<m:
        m=abs(ave-a[i])
        x=i
print(x)