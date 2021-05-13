n = int(input())
A = tuple(map(int, input().split()))
ae = A[::2]
ao = A[1::2]

if n%2 == 0:
    print(*(ao[::-1] + ae))
else:
    print(*(ae[::-1] + ao))
