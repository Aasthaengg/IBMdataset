n = int(input())
A = list(map(int,input().split()))
if n%2==0:
    a = A[::2]
    b = A[1::2]
    b = b[::-1]
    print(*(b+a))
else:
    a = A[::2]
    a = a[::-1]
    b = A[1::2]
    print(*(a+b))