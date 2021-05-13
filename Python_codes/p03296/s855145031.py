n=int(input())
a=list(map(int,input().split()))

cnt=0
temp=1
pre_str=a[0]
for i in range(1,n):
    if a[i]==pre_str:
        temp+=1
    else:
        pre_str=a[i]
        temp=1

    if temp%2==0:
        cnt+=1
print(cnt)
