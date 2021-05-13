n=int(input())
a=list(map(int,input().split()))
b=[0 for i in range(9)]
for i in range(n):
    b[min([a[i]//400,8])]+=1

ans1=len([i for i in b[:8] if i>0])
ans2=ans1+b[8]
ans1=max([ans1,1])
print(ans1,ans2)
