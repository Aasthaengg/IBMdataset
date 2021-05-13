N,M,D = list(map(int,input().split()))
if D!=0:
    print((2 * (N-D) * (M-1))/(N**2))
else:
    print(((N-D) * (M-1))/(N**2))