N,M = map(int,input().split())
if N > 9:
    print(M)
else:
    print(M + (100 * (10-N)))