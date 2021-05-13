N,A,B=map(int, input().split())
V=list(map(int, input().split()))
d={}
for v in V:
    if v in d:
        d[v]+=1
    else:
        d[v]=1
k=sorted(d.keys(),reverse=True)
def comb1(n,k):
    if n<k:
        return 0
    if n<0 or k<0:
        return 0
    k=min(n-k,k)
    a=b=1
    for i in range(1,k+1):
        a=a*(n-k+i)
        b=b*i
    return a//b
ans=0
if d[k[0]]>=A:
    for x in range(A,min(B,d[k[0]])+1):
        ans+=comb1(d[k[0]],x)
    ave=k[0]
else:
    n=d[k[0]]
    a=[k[0]]*d[k[0]]
    for i in range(1,len(k)):
        if n+d[k[i]]>=A:
            break
        else:
            n+=d[k[i]]
            a+=[k[i]]*d[k[i]]
    ans=comb1(d[k[i]],A-n)
    a+=[k[i]]*(A-n)
    from statistics import mean
    ave=mean(a)
print(ave)
print(ans)