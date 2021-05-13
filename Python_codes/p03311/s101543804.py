n=int(input())
a=list(map(int,input().split()))
l=[0]*n
for i in range(1,n+1):
    l[i-1]=a[i-1]-i
l.sort()
ans=0
if n%2==1:
    for i in range(n):
        ans+=abs(l[i]-(l[n//2]))
    print(ans)
else:
    ans_1=0
    ans_2=0
    for i in range(n):
        ans_1+=abs(l[i]-(l[n//2-1]))
    for i in range(n):
        ans_2+=abs(l[i]-(l[n//2]))
    print(min(ans_1,ans_2))