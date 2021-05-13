n=int(input())
a=list(map(int,input().split()))
a=sorted(a)
sum_=[]
total=0
for i in range(n):
    total+=a[i]
    sum_.append(total)
a=sorted(a,reverse=True)
ans=1
max_=a[0]
for i in range(1,n):
    if max_<=a[i]*2:
        ans+=1
        max_=a[i]
    else:
        if max_<=sum_[(n-1)-i]*2: #自分以下の数を吸収
            ans+=1
            max_=a[i]
        else:
            break
print(ans)