n,k=map(int,input().split())
ret=[str(i)+' 1'for i in range(2,n+1)]

m=(-2+n)*(n-1)//2-k
if m<0:print(-1);exit()
now=2
j=3
print(len(ret)+m)
while m:
    ret.append(str(now)+' '+str(j))
    j+=1
    if j==n+1:
        j=now+2
        now+=1
    m-=1
print("\n".join(ret))
