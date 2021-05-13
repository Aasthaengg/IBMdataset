n=int(input())
a=list(map(int,input().split()))
ans1=0
ans2=0
flg=True
t=0
for i in range(n):
    t+=a[i]
    if flg:
        if t<=0:
            ans1+=1-t
            t=1
        flg=False
    else:
        if t>=0:
            ans1+=t+1
            t=-1
        flg=True
t=0
flg=True
for i in range(n):
    t+=a[i]
    if flg==False:
        if t<=0:
            ans2+=1-t
            t=1
        flg=True
    else:
        if t>=0:
            ans2+=t+1
            t=-1
        flg=False
print(min(ans1,ans2))