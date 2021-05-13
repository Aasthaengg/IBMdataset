import heapq as h

def partions(M):#Mの約数列 O(n^(0.5+e))
    import math
    d=[]
    i=1
    while math.sqrt(M)>=i:
        if M%i==0:
            d.append(i)
            if i**2!=M:
                d.append(M//i)
        i=i+1
    d.sort()
    return d


N,K=map(int,input().split())
A=list(map(int,input().split()))
s=sum(A)
candidate=partions(s)
ans=1
for i in range(0,len(candidate)):
    X=[A[j]%candidate[i] for j in range(0,N)]
    s=sum(X)//candidate[i]
    test=0
    h.heapify(X)
    for j in range(0,N-s):
        test=h.heappop(X)
    test=candidate[i]*s-sum(X)
    if K>=test:
        ans=candidate[i]
print(ans)
