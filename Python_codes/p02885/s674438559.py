A, B = map(int, input().split())

N = A - 2 * B

if N > 0:
    print(str(N))
else:
    print(0)