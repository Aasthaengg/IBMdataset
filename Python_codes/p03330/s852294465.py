N, C = map(int, input().split())

D = [list(map(int, input().split())) for _ in range(C)]

c = [list(map(int, input().split())) for _ in range(N)]

group = [[0] * C for _ in range(3)]
for i in range(N):
    for j in range(N):
        group[(i + j) % 3][c[i][j] - 1] += 1

def calc(g, color): #g: groupをcolorに変える違和感を返す
    cost = 0
    for i in range(C):
        cost += group[g][i] * D[i][color]
    return cost

# for i in group:
#     print (i)

ans0 = []
for i in range(C):
    ans0.append((calc(0, i), i))
ans0.sort()

ans1 = []
for i in range(C):
    ans1.append((calc(1, i), i))
ans1.sort()

ans2 = []
for i in range(C):
    ans2.append((calc(2, i), i))
ans2.sort()

# print (ans0)
# print (ans1)
# print (ans2)

ans = 10 ** 18
for i in range(3):
    for j in range(3):
        for k in range(3):
            if ans0[i][1] != ans1[j][1] and ans1[j][1] != ans2[k][1] and ans2[k][1] != ans0[i][1]:
                ans = min(ans, ans0[i][0] + ans1[j][0] + ans2[k][0])

print (ans)