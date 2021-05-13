n=int(input())
a=list(map(int,input().split()))
b=(sum(a))/2
count=0
if n==2:
    ans=int(abs((b-a[0])*2))
else:
    for i in range(n):
        count+=a[i]
        if b<=count:
            if i==0:
                c=count
                d=count+a[i+1]
            else:
                c=count-a[i]
                d=count
            break
    e=min(abs(c-b),abs(d-b))
    ans=int(e*2)
print(ans)
