N=int(input())

A=list(map(int,input().split()))

NA=[]

cnt=0
d={}
for i in range(N):
    if A[i]-i in d:
        cnt+=d[A[i]-i]
    if not -A[i]-i in d:
        d[-A[i]-i]=1
    else:
        d[-A[i]-i]+=1

print(cnt)

