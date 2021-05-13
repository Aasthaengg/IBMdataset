n=int(input())
a=list(map(int,input().split()))
tmp=float("inf")
flg=True
b=list(map(lambda x:abs(x),a))
ans=sum(b)
t=sum(b)
for i in range(n):
    if a[i]==0:
        print(ans)
        exit()
    if a[i]<0:
        if flg:
            flg=False
        else:
            flg=True
    if abs(a[i])<tmp:
        tmp=abs(a[i])
if flg:
    print(ans)
else:
    print(ans-2*tmp)