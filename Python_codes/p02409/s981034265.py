home = [[[0 for r in range(10)] for f in range(3)] for b in range(4)]
n = int(raw_input())
for i in range(n):
    b, f, r, v = map(int, raw_input().split())
    home[b-1][f-1][r-1] += v

for i in range(4):
    for j in range(3):
        print "",
        print " ".join(map(str, home[i][j]))
        if j == 2 and i != 3:
            print "#" * 20
