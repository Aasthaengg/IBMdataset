N,M = map(int,input().split())
if N > M:
    N,M = M,N
if N == 1:
    print(1 if M==1 else M-2)
elif N == 2:
    print(0)
else:
    print((N-2) * (M-2))
