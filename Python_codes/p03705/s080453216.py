N, A, B = map(int, input().split())

if (A > B):
    print(0)
    exit()
elif (B > A and N == 1):
    print(0)
    exit()
elif (A == B and N == 1):
    print(1)
    exit()
else:
    ma = B * (N - 2)
    mi = A * (N - 2)
    print(ma - mi + 1)
