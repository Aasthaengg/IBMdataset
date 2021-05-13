N,M = map(int, input().split())
L = [list(map(int,input().split())) for _ in range(M)]
L.sort(key=lambda x: x[0])
funes1 = [False]*N
for a,b in L:
    if a == 1:
        funes1[b] = True
    else:
        if funes1[a]:
            if b == N:
                print('POSSIBLE')
                exit()
print('IMPOSSIBLE')