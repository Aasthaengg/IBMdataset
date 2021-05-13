D, N = map(int, input().split())

if (N == 100):
    print((N * (100 ** D)) + 100**D)
else:
    print(N * (100 ** D))
