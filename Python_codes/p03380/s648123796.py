N = int(input())
A = list(map(int,input().split()))

A.sort()
n = A[-1]

r_=n/2

a_before=''
for a in A[:-1]:
    if a >= r_:
        break
    a_before = a
    
if abs(r_-a) >= abs(r_-a_before):
    r = a_before
else:
    r = a
    
print(n,r)