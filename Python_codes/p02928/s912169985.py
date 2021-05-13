n,k=map(int,input().split())
lst=list(map(int,input().split()))
ans=0
for i in range(n):
    judge=lst[i]
    front=lst[:i]
    back=lst[i+1:]
    former=0
    latter=0
    for j in front:
        if j>judge:
            former+=1
    for j in back:
        if j>judge:
            latter+=1
    ans+=(former*((k+1)*k//2)+latter*((k-1)*k//2))
    ans%=(10**9+7)
print(ans)