N, M = [int(x) for x in input().split()]

cond = [None for _ in range(N + 1)]
ok = True
for i in range(M):
    s, c = [int(x) for x in input().split()]
    if cond[s] == None:
        cond[s] = c
    else:
        if cond[s] != c:
            ok = False
            break

if cond[1] == None:
    if N == 1:
        cond[1] = 0
    else:
        cond[1] = 1
else:
    if cond[1] == 0:
        if N != 1:
            ok = False

for i in range(2, N + 1):
    if cond[i] == None:
        cond[i] = 0

if ok == True:
    for i in range(1, N + 1):
        print(cond[i], end='')
    print('')
else:
    print(-1)