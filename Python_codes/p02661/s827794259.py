#E
N = int(input())
A = []
B = []
for i in range(N):
    a,b = map(int,input().split())
    A.append(a)
    B.append(b)
A.sort()
B.sort()
if N%2 == 0:
    n = int(N/2)
    xmin = (A[n-1]+A[n])
    xmax = (B[n-1]+B[n])
    count = int(xmax)-int(xmin+0.5)+1
else:
    n = int((N+1)/2)
    xmin = A[n-1]
    xmax = B[n-1]
    count = xmax-xmin+1

print(count)