N, K = map(int,input().split())
P = N % K
if P != 0:
    print(1)
else:
    print(0)