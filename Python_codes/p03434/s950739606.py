N=int(input())
A=list(map(int,input().split()))

A=sorted(A)[::-1]
a=0
b=0

for i in range(N):
    if i%2==0:
        a+=A[i]
    else:
        b+=A[i]
        
print(a-b)