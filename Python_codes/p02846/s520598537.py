*T, = map(int,input().split())
*A, = map(int,input().split())
*B, = map(int,input().split())

if A[0]*T[0]+A[1]*T[1] == B[0]*T[0]+B[1]*T[1]:
    print("infinity")
else:
    if A[0]<B[0] : A,B = B,A
    if A[0]*T[0]+A[1]*T[1] > B[0]*T[0]+B[1]*T[1] :
        print(0)
    else:
        L = (A[0]-B[0]) * T[0]
        d = -((A[0]-B[0]) * T[0] + (A[1]-B[1]) * T[1])
        ans = L//d*2 + (L%d>0)
        print(ans)