n=int(input())
a=list(map(int, input().split()))
b=list(map(int, input().split()))

a_sum=sum(a)
b_sum=sum(b)

if a_sum<b_sum:
    ans=-1
else:
    dif=[0]*n
    dif_sum=a_sum-b_sum
    ans=n
    for i in range(n):
        dif[i]=a[i]-b[i]
    dif.sort()
    for d in dif:
        if d>=0:
            dif_sum-=d
            if dif_sum<0:
                break
            ans-=1
    
print(ans)