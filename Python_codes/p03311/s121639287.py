n=int(input())
a=list(map(int,input().split()))
aa=[a[i-1]-i for i in range(1,n+1)]


aaa=sorted(aa)
if len(aaa)%2==0:
    m1=aaa[len(aaa)//2]
    m2=aaa[len(aaa)//2-1]
else:
    m1=aaa[len(aaa)//2]
    m2=m1
ans1,ans2=0,0
for i in aa:
    ans1+=abs(i-m1)
    ans2+=abs(i-m2)
print(min(ans1,ans2))