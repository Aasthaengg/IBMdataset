N=int(input())
A=list(map(int,input().split()))
counter=1
res=0
for i in range(len(A)-1):
    if (A[i+1]<A[i] and res>0) or (A[i+1]>A[i] and res<0):
        counter+=1
        res=0
    elif A[i+1]!=A[i]:
        res=A[i+1]-A[i]


print(counter)
