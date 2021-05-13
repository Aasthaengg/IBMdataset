n=int(input())
a1=list(map(int,input().split()))
a2=sorted([a1[i-1]-i for i in range(1,n+1)])
if len(a2)%2==0:
    m1=a2[len(a2)//2]
    m2=a2[len(a2)//2-1]
else:
    m1=a2[len(a2)//2]
    m2=m1
ans1,ans2=0,0
for i in a2:
    ans1+=abs(i-m1)
    ans2+=abs(i-m2)
print(min(ans1,ans2))