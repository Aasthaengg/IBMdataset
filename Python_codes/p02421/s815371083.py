N = int( input() )

AP = 0
BP = 0


for i in range(N):
    A,B = input().split()
    sa = 0
    X = max( len(A) , len(B) )
    A = A.ljust(X, '0')
    B = B.ljust(X, '0')
    if A == B:
        AP += 1
        BP += 1
    else:
        for j in range(X):
            if ord( A[j] ) > ord( B[j] ):
                AP += 3
                break
            elif ord( B[j] ) > ord( A[j] ):
                BP += 3
                break
            else:
                pass
print( AP,BP, sep=' ')
