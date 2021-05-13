N, M = map(int,input().split())

L, R = 1, N

for _ in range(M):
    l, r = map(int,input().split())

    if(r < L or R < l):
        print(0)
        exit()
    else:
        L = max(l,L)
        R = min(r,R)

print(R-L+1)
