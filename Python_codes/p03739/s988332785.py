n = int(input())
a = list(map(int,input().split()))

b = [0]*n
b[0]=a[0]
pt = 0
m = 0
ans1 = 0
ans2 = 0
for i in range(1,n):
    b[i]=b[i-1]+a[i]

for i in range(n):
    if i%2==0 and b[i]+m<=0:
        ans1+=1-b[i]-m
        m+=1-b[i]-m
    elif i%2==1 and b[i]+m>=0:
        ans1+=1+b[i]+m
        m+=-1-b[i]-m
m=0
for i in range(n):
    if i%2==1 and b[i]+m<=0:
        ans2+=1-b[i]-m
        m+=1-b[i]-m
    elif i%2==0 and b[i]+m>=0:
        ans2+=1+b[i]+m
        m+=-1-b[i]-m
print(min(ans1,ans2))
