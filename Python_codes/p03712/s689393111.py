H,W=list(map(int,input().split()))
cell = '#'*(W+2)
cells = [cell]
s = '#'
for i in range(H):
    a = s+input()+s
    cells.append(a)
cells.append(cell)
for c in cells:
    print(c)
