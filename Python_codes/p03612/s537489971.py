n=int(input())
a=list(map(int,input().split()))

cnt=0
i=0
while i<n:
    if i!=n-1:
        if i+1==a[i]:
            cnt+=1
            i+=2
        else:
            i+=1
    else:
        if i+1==a[i]:
            cnt+=1
        i+=1
print(cnt)
        


