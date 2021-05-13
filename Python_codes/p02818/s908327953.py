A, B, K = map(int, input().split())

if K <= A:
    print(A - K)
    print(B)

elif K > A and (B - (K - A)) > 0:
    print(0)
    print(B - (K - A))

else:
    print(0)
    print(0)