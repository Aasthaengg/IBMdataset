n=int(input())
*b,=map(int,input().split())
a=[0]+b+[0]
sum=0
for i in range(n+1):
    sum+=abs(a[i+1]-a[i])
for i  in range(n):
    print(sum-abs(a[i+1]-a[i])-abs(a[i+2]-a[i+1])+abs(a[i+2]-a[i]))