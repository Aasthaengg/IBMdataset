h, w = map(int, input().split())
hw = [list(input()) for _ in range(h)]
num = 0
for i in range(h):
    num+=hw[i].count('#')

def check(i, j):
    if not (0<=i<h and 0<=j<w):
        return False
    if hw[i][j] == '#':
        return True
    return False

checked = set()
for i in range(h):
    for j in range(w):
        if hw[i][j] == '#':
            if (i,j) in checked:
                continue

            exist = False

            for di,dj in [(1,0),(-1,0),(0,1),(0,-1)]:
                ci = i + di
                cj = j + dj
                if check(ci, cj):
                    checked.add((ci,cj))
                    exist = True
            if exist:
                checked.add((i,j))
if num == len(checked):
    print('Yes')
else:
    print('No')