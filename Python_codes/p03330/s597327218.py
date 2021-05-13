N, C = map(int, input().split())
D = [list(map(int, input().split())) for i in range(C)]
c = [list(map(int, input().split())) for i in range(N)]

G1 = [0]*C
G2 = [0]*C
G3 = [0]*C
a = int(0)

for i in range(N):
    for j in range(N):
        if (i + j) % 3 ==2:
            G1[c[i][j]-1] += 1
        elif (i + j) % 3 == 0:
            G2[c[i][j]-1] += 1
        else:
            G3[c[i][j]-1] += 1
ans_candi = []


for i1 in range(C):
    for i2 in range(C):
        for i3 in range(C):
            t = int(0)
            if i1!=i2 and i2!=i3 and i3!=i1:
                for j in range(C):
                    t += D[j][i1]*G1[j]
                for j in range(C):
                    t += D[j][i2]*G2[j]
                for j in range(C):
                    t += D[j][i3]*G3[j]
                ans_candi.append(t)

print(min(ans_candi))