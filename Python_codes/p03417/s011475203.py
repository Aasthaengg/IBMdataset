N,M = map(int,input().split())
if N >= 3 and M >= 3:
    print((N-2)*(M-2))
elif N == 2 or M == 2:
    print(0)
else:
    print(max(1,N-2)*max(1,M-2))