N=int(input())
A=list(map(int,input().split()))
i=0
a=1
t=0
while i<N-1:
    if A[i]<A[i+1]:
        if t==-1:
            a+=1
            t=0
        elif not t:
            t=1
    elif A[i]>A[i+1]:
        if t==1:
            a+=1
            t=0
        elif not t:
            t=-1
    i+=1
print(a)