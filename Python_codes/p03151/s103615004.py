import sys

n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))

sum_a=sum(a)
sum_b=sum(b)
c=[]
cnt=0
ans=0
d=0
if(sum_a<sum_b):
    print(-1)
else:
    for i in range(n):
        if a[i]<b[i]:
            cnt+=1
            d+=(b[i]-a[i])
        else:
            c.append(a[i]-b[i])
    if cnt==0:
        print(cnt)
        sys.exit()
    cc=sorted(c,reverse=True)
    cc_sum=0
    for i in range(n):
        cc_sum+=cc[i]
        if cc_sum>d:
            cnt+=(i+1)
            break
    print(cnt)