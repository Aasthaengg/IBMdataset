n=int(input())
a=list(map(int,input().split()))
ans1=max(a)
m=10**9+1
temp=ans1/2
i=0
for index,val in enumerate(a):
    if val==ans1: continue
    if abs(val-temp)<m:
        m=abs(val-temp)
        i=index
ans2=a[i]
print(ans1,ans2)