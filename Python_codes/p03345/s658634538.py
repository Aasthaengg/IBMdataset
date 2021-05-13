A, B, C, K = list(map(int, input().split()))

if K % 2 != 0:
    r = B - A
else:
    r = A - B

if abs(r) > 10 ** 18:
    print('Unfair')
else:
    print(r)