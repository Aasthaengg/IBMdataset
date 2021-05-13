n=int(input())
a=list(map(int,input().split()))
ans=0
for i in range(0,len(a)):
    ans=ans+(1/a[i])
print(1/ans)