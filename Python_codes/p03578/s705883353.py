N = int(input())
D = sorted(list(map(int, input().split())))
M = int(input())
T = sorted(list(map(int, input().split())))

if N < M:
    print('NO')
    exit()

fnd = 0
nw = 0
isok = True
for t in T:
    for i in range(nw, N):
        nw += 1
        if t == D[i]:
            fnd += 1
            break
        elif t < D[i]:
            isok = False
            break

print('YES' if (isok and fnd==len(T)) else 'NO')