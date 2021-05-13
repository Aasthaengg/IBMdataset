A, B, C, K = map(int, input().split())

if K % 2 == 0:
    if A - B > 10e18:
        print('Unfair')
    else:
        print(A - B)
else:
    if B - A > 10e18:
        print('Unfair')
    else:
        print(B - A)