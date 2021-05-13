A, B, N = map(int, input().split())
if N < B:
    print(A*N//B)
else:
    x = B - 1
    print((A*x)//B)