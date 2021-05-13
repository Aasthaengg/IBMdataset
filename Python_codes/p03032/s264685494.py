from collections import deque
N,K=map(int,input().split())
V=list(map(int,input().split()))
res=0
for i in range(min(K,N)+1):
    for L in range(i+1):
        R=i-L
        li=[]
        for j in range(L):
            li.append(V[j])
        for j in range(R):
            li.append(V[N-j-1])
        li.sort()
        s=sum(li)
        for k in range(min(K-i,len(li))):
            if(li[k]<0):
                s-=li[k]
            else:
                break
        res=max(s,res)
print(res)