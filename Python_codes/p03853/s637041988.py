H, W = map(int, input().split())
C = []
for _ in range(H):
    C.append(list(input()))

D = []
for i in range(2*H):
    D.append(C[i//2])
    print(''.join(D[i]))
