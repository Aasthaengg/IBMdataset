N,M = map(int,input().split())
if N == 1 and M == 1:
    print(1)
else:
    print(abs((N-2)*(M-2)))