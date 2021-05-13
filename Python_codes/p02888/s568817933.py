from bisect import bisect_left
n=int(input())
lst=sorted(map(int,input().split()))
ans=0
for i in range(n):
    for j in range(i+1,n):
        p=lst[i]+lst[j]
        out=bisect_left(lst,p)
        ans+=(out-j-1)
print(ans)