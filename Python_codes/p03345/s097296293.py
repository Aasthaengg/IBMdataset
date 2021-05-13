A, B, C, K = map(int, input().split())

m = A - B
n = B - A

if (K % 2 == 0):
    if m > 10**18:
        print('Unfair')
    print(m)
else:
    if (n > 10**18):
        print('Unfair')
    print(n)
