A, B, C, K = map(int, input().split())

if A == B == C:
    print(0)
elif K == 0:
    if A - B > 10e18:
        print('Unfair')
    else:
        print(A - B)
else: 
    if K % 2 == 0:
        a = K*A + (K-1)*(B+C)
        b = K*B + (K-1)*(A+C)
        c = K*C + (K-1)*(A+B)
    else:
        a = (K-1)*A + K*(B+C)
        b = (K-1)*B + K*(A+C)
        c = (K-1)*C + K*(A+B)
    
    if a - b > 10e18:
        print('Unfair')
    else:
        print(a - b)