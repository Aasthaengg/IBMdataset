
# ABC138
# B One Clue
# K個連続黒、Xが黒、座標-1000000+1000000
k, x = map(int, input().split())
L = []
for i in range(k):
    y = x + i
    z = x - i
    if y > 1000000:
        y = x
    L.append(y)
    if z < -1000000:
        z = x
    L.append(z)
I = set(L)
L = list(sorted(I))
for s in L:
    print(s,end = " ")
