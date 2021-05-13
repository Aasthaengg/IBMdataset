S, M = map(int,input().split())
if S < 10:
    print(M + 100 * (10 - S))
else:
    print(M)

