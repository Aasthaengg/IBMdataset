c = [list(map(int,input().split())) for _  in range(3)]
d = set()
e = set()
for i in range(3):
    d.add(c[i][0] - c[i][1])
    e.add(c[i][1] - c[i][2])
print("Yes" if len(d) == len(e) == 1 else "No")