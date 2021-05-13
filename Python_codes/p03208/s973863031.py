N,K = (int(X) for X in input().split())
H = sorted(int(input()) for X in range(0,N))
MIN = pow(10,9)
for T in range(0,N-K+1):
    D = H[T+K-1]-H[T]
    if D<MIN: MIN = D
print(MIN)