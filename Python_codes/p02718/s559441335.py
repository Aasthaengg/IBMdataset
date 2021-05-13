n,m=map(int,input().split())
a=list(map(int,input().split()))
cnt=0
suma=sum(a)
for i in range(n):
    if a[i]>=suma/4/m:
        cnt+=1
if cnt>=m:
    print("Yes")
else:
    print("No")
