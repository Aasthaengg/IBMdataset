C = [[int(i) for i in input().split()] for _ in range(3)]

D = [[] for _ in range(4)]
for i in range(2):
    for j in range(3):
        D[i].append(C[i+1][j] - C[i][j])
        D[i+2].append(C[j][i+1] - C[j][i])

for d in D:
    if len(set(d)) != 1:
        print("No")
        break
else:
    print("Yes")