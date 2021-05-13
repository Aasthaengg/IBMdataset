N = int(input())
A = sorted([int(i) for i in input().split()])

if max(A) < 0:
    print(max(A)-sum(A[:-1]))
    c = max(A)
    for i in range(N-1):
        print(c, A[i])
        c -= A[i]

elif min(A) >= 0:
    print(sum(A[1:])-min(A))
    c = min(A)
    for i in range(1, N-1):
        print(c, A[i])
        c -= A[i]
    print(max(A), c)

else:
    print(sum(abs(x) for x in A))
    c = min(A)
    d = max(A)
    for i in range(1, N-1):
        if A[i] < 0:
            print(d, A[i])
            d -= A[i]
        else:
            print(c, A[i])
            c -= A[i]
    print(d, c)
    
