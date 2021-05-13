n = int(input())

A = [0]*n
B = [0]*n
for i in range(n):
    A[i], B[i] = map(int,input().split())

A.sort()
B.sort()

#print(A)
#print(B)

if n%2:
    a = A[(n+1)//2-1]
    b = B[(n+1)//2-1]
    print(int(b-a+1))
else:
    a = (A[n//2-1]+A[n//2])/2
    b = (B[n//2-1]+B[n//2])/2
    print(int((b-a)*2+1))
