h,n=map(int,input().split())
a=list(map(int,input().split()))
gokei=0
ans="No"
for i in range(n):
    gokei+=a[i]
    if gokei>=h:
        ans="Yes"
print(ans)