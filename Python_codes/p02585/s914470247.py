from math import inf
n,k=map(int,input().split())
arr=[0]+list(map(int,input().split()))
cost=[0]+list(map(int,input().split()))
ma=-inf
for i in range(1,n+1):
    se=set()
    cur=i
    pref=[0]
    f=0
    while(cur not in se and f<k):
        se.add(cur)
        cur=arr[cur]
        co = cost[cur]
        pref.append(pref[-1]+co)
        ma=max(ma,pref[-1])
        f+=1

    if pref[-1]>0 and k>=f:
        ans=pref[-1]*(k//f)
        for j in range(k%f+1):
            ma=max(ma,ans+pref[j])
        ma=max(ma,pref[-1]*(k//f-1)+max(pref))
print(ma)









