N,T=map(int,input().split())
A=list(map(int,input().split()))
t=0
k=A[0]
c=0
for i in A:
    if i<k:
        k=i
    elif i-k>t:
        t=i-k
        c=1
    elif i-k==t:
        c+=1
print(c)