l = [list(map(int,input().split())) for _ in range(3)]
# print(l)
l1 = []
for i in range(3):
    l1.append(tuple(j - min(l[i]) for j in l[i]))
if len(set(l1)) != 1:
    print('No')
    exit()

k = [[0]*3 for _ in range(3)]
for i in range(3):
    for j in range(3):
        k[j][i] = l[i][j]
k1 = []
for i in range(3):
    k1.append(tuple(j - min(k[i]) for j in k[i]))
if len(set(k1)) != 1:
    print('No')
    exit()

print('Yes')