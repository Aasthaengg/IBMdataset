import itertools
n,c = map(int,input().split())
D = [list(map(int,input().split())) for _ in range(c)]
C = [list(map(int,input().split())) for _ in range(n)]
mod0 = []
mod1 = []
mod2 = []
for i in range(n):
    for j in range(n):
        # indexのずれを考慮 ((i+1)+(j+1))%3が本来のmod値
        if (i+j)%3 == 1:
            mod0.append(C[i][j]-1)
        elif (i+j)%3 == 2:
            mod1.append(C[i][j]-1)
        else:
            mod2.append(C[i][j]-1)

conv_0, conv_1, conv_2 = [],[],[]
for i in range(c):
    tmp0, tmp1, tmp2 = 0,0,0
    for j in range(len(mod0)):
        tmp0 += D[mod0[j]][i]
    for j in range(len(mod1)):
        tmp1 += D[mod1[j]][i]
    for j in range(len(mod2)):
        tmp2 += D[mod2[j]][i]
    conv_0.append(tmp0)
    conv_1.append(tmp1)
    conv_2.append(tmp2)
res = float('inf')
for x,y,z in itertools.permutations(list(range(c)), 3):
    cnt = conv_0[x] + conv_1[y] + conv_2[z]
    res = min(cnt, res)
print(res)