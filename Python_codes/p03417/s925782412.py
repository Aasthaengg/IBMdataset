N,M = (int(X) for X in input().split())
if N==1 or M==1:
    if N==M: print(1)
    else: print(max(N,M)-2)
else: print((N-2)*(M-2))