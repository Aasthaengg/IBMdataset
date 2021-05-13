A, B, C, K = map(int, input().split())

if K == 0:
    print(A-B)
    exit()

A, B, C = B+C, C+A, A+B

if abs(A-B) > 10**18:
    print('Unfair')
else:
    if K % 2 == 1:
        print(A-B)
    else:
        print(-(A-B))