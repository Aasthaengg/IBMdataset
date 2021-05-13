n=int(input())
a=list(map(int,input().split()))
q=int(input())
b=[]
c=[]
for i in range(q):
    tempb,tempc=map(int,input().split())
    b.append(tempb)
    c.append(tempc)
cnt=[-1]+[0]*10**5
for i in range(n):
    cnt[a[i]]+=1
ans=sum(a)
for i in range(q):
    ans+=(c[i]-b[i])*cnt[b[i]]
    cnt[c[i]]+=cnt[b[i]]
    cnt[b[i]]=0
    print(ans)