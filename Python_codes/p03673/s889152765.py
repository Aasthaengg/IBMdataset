n = int(input())
A = list(map(int,input().split()))
if n%2==0:
    B = A[1::2]
    C = A[::2]
    B = B[::-1]
    print(*(B+C))
else:
    B = A[::2]
    C = A[1::2]
    B = B[::-1]
    print(*(B+C))