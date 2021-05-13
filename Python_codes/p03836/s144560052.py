import copy

sx, sy, tx, ty = map(int, input().split())
p = [sx, sy]
g = []
b = []

for _ in range(1,tx - sx):
    g.append('R')
    b.append('L')
for _ in range(1,ty - sy):
    g.append('U')
    b.append('D')

b.reverse()

g1 = g
g1.insert(0,'R')
g1.append('U')
g2 = copy.deepcopy(g1)
g2.insert(0,'R')
g2.insert(0,'D')
g2.append('U')
g2.append('L')
b1 = b
b1.insert(0,'L')
b1.append('D')
b2 = copy.deepcopy(b1)
b2.insert(0,'L')
b2.insert(0,'U')
b2.append('D')
b2.append('R')

ans = []
ans.extend(g1)
ans.extend(b1)
ans.extend(g2)
ans.extend(b2)
ans = ''.join(ans)
print(ans)