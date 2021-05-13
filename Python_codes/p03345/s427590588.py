A, B, C, K = map(int, input().split())

if abs(A-B) > 10**18:
    print('unfair')
else:
    if K % 2 == 0:
        print(A-B)
    else:
        print((A-B)*(-1))