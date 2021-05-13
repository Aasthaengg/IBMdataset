n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
a_s=sum(a)
b_s=sum(b)
if a_s>b_s:
    print("No")
    exit()
count=b_s-a_s
temp1=0
temp2=0
for i in range(n):
    if a[i]>=b[i]:
        temp1+=a[i]-b[i]
    else:
        if a[i]%2==b[i]%2:
            temp2+=(b[i]-a[i])//2
        else:
            temp1+=1
            temp2+=(b[i]+1-a[i])//2

if temp1>count or temp2>count:
    print("No")
    exit()
if (count-temp1)==(count-temp2)*2:
    print("Yes")
else:
    print("No")