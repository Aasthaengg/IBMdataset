# ABC175 D
import bisect

N,K=map(int,input().split())
P=list(map(int,input().split()))
C=list(map(int,input().split()))

F=[0]*N

def search(n):
    res=[]
    l=0
    m=n
    tmp_res=0
    isloop=0
    if F[n-1]:
        s,L=F[n-1]
    while 1:
        m=P[m-1]
        tmp_res+=C[m-1]
        l+=1
        if F[n-1]==0:
            res.append((tmp_res,l))
        else:
            res.append(tmp_res+s*((K-l)//L) if s>0 and K>=l else tmp_res)
        if m==n:
            isloop=1
            break
        if l==K:
            break
    if F[n-1]==0:
        if isloop:
            s,L=res[-1]
            if not F[n-1]:
                m=n
                while 1:
                    F[m-1]=(s,L)
                    m=P[m-1]
                    if m==n:
                        break
        else:
            s=-1
        p=max([p+s*((K-k)//len(res)) if s>0 and K>=k else p for p,k in res])
    else:
        p=max(res)
    return p

res=-float('inf')
for i in range(N):
    res=max(res,search(i+1))
print(res)