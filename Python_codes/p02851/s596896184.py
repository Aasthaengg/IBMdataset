N,K=map(int,input().split())
A=list(map(int,input().split()))

for i in range(1,N):
    A[i]+=A[i-1]

A.append(0)
A.sort()

A=[((A[i]-i)%K,i) for i in range(0,N+1)]
A.sort()
count=0
s=0
t=1
while N>=t and N>=s:
    if A[t][0]==A[s][0] and K>A[t][1]-A[s][1]:
        t+=1
        if t==N+1:
            count+=((t-s)*(t-s-1))//2
    else:
        count+=t-s-1
        s+=1
        if s==t:
            t+=1

print(count)