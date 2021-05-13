import sys

lines = [list(map(int,line.split())) for line in sys.stdin]
r,c = lines[0]

lines = lines[1:]
for i,row in enumerate(lines):
    lines[i].append(sum(row))

lines.append([])
for i in range(c+1):
    s = 0
    for j in range(r):
        s+=lines[j][i]
    lines[-1].append(s)

for l in lines:
    print(" ".join(map(str,l)))