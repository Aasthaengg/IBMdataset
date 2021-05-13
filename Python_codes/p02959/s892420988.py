#<ABC.C>
#<135>
N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

ans = 0
for i in range(N):
    A[i] -= B[i]
    if A[i] <= 0:
        ans += A[i] + B[i]
        B[i] = - A[i]
        A[i] = 0
        A[i + 1] -= B[i]
        if A[i + 1] <= 0:
            ans += A[i + 1] + B[i]
            #B[i] =  -A[i + 1]
            A[i + 1] = 0
            #B[i] = 0
        else:
            ans += B[i]
            B[i] = 0
    else:
        ans += B[i]
        B[i] = 0
    #print(A)
    #print(B)
print(ans)
             
