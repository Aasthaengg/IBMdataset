n = int(input())
table = [[[0 for i in range(10)] for j in range(3)] for k in range(4)]

for l in range(n):
    b, f, r, v = map(int, input().split())
    table[b-1][f-1][r-1] += v

k = 0
for i in range(4):
    for j in range(3):
        output = " ".join(map(str, table[i][j]))
        print(" %s" % output)
    if k < 3:
        print("####################")
        k += 1