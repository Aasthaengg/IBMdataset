h, w = map(int,input().split())
S = [input() for i in range(h)]

M = [[] for i in range(h*w)]

for i in range(h*w):
    a = i // w
    b = i % w
    for d in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
        aa = d[0] + a
        bb = d[1] + b
        if 0 <= aa < h and 0 <= bb < w \
            and S[a][b] != S[aa][bb]:
            M[a*w+b].append(aa*w+bb)

# print(M)

ans = 0
V = [0] * (h*w)
D = {".":0, "#":1}
for i in range(h*w):
    if V[i] == 0:
        ANS = [0, 0]
        Q = [i]
        s = 0
        V[i] = 1
        ANS[D[S[i//w][i%w]]] += 1
        while s < len(Q):
            i = Q[s]
            for x in M[i]:
                if V[x] == 0:
                    V[x] = 1
                    ANS[D[S[x//w][x%w]]] += 1
                    Q.append(x)
            s += 1
        # print(ANS)
        ans += ANS[0] * ANS[1]
print(ans)