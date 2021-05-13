import sys

n=int(input())
A=list(map(int,input().split()))
A.sort()

if n==2:
    print(A[1],A[0])
    sys.exit()

p=A[-1]
h=p/2
for i in range(n-1):
    if A[i]>=h:
        break
if abs(A[i-1]-h)<=abs(A[i]-h):
    q=A[i-1]
else:
    q=A[i]
print(p,q)