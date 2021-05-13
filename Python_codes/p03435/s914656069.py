c = [list(map(int,input().split())) for _  in range(3)]
d = set()
e = set()
f = set()
g = set()
for i in range(3):
    d.add(c[i][0] - c[i][1])
    e.add(c[i][1] - c[i][2])
    f.add(c[0][i] - c[1][i])
    g.add(c[1][i] - c[2][i])
if len(d) == len(e) == len(f) == len(g) == 1:
    print("Yes")
else:
    print("No")