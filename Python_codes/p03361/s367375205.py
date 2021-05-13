h, w = map(int, input().split())
cells = []
for i in range(h):
    s = input().split()
    cells.append(s[0])
ans = True
for i in range(1,h-1):
    for j in range(1,w-1):
        if cells[i][j] == '#':
            if cells[i-1][j] != '#' and cells[i+1][j] != '#' and cells[i][j-1] != '#' and cells[i][j+1] != '#':
                ans = False
                break
 
if ans: print("Yes")
else: print("No")