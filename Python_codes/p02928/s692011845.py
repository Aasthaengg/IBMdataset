n,k=map(int,input().split())
M=10**9+7
a=list(map(int,input().split()))
cnt=[[0 for i in range(2)] for j in range(n)]
for i in range(n):
    for j in range(n):
        if j<i and a[j]<a[i]:
            cnt[i][0]+=1
        elif i<j and a[j]<a[i]:
            cnt[i][1]+=1
sum=0
for i in range(n):
    s=((k*(cnt[i][0]+cnt[i][1])+(cnt[i][1]-cnt[i][0]))*k)//2
    sum+=s
    sum%=M
print(sum)
