N,M=map(int,input().split())
A=list(map(int,input().split()))
a=0
for i in A:
    a+=i
b=a/(4*M)
c=0
for n in range(0,N):
    if A[n]>=b:
        c+=1
if c>=M:
    print('Yes')
else:
    print('No')

