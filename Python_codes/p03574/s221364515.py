#n = int(input())
h, w = map(int,input().split())
#l = list(map(int,input().split()))
l = [list(input()) for i in range(h)]
def possible(i, j):
    if i == -1 or i == h:
        return False
    if j == -1 or j == w:
        return False    
    return True

for i in range(h):
    for j in range(w):
        count = 0
        if l[i][j] == '.':
            if possible(i-1, j) and l[i-1][j] == '#':
                count += 1
            if possible(i+1, j) and l[i+1][j] == '#':
                count += 1
            if possible(i, j+1) and l[i][j+1] == '#':
                count += 1
            if possible(i, j-1) and l[i][j-1] == '#':
                count += 1
            if possible(i-1, j+1) and l[i-1][j+1] == '#':
                count += 1
            if possible(i+1, j+1) and l[i+1][j+1] == '#':
                count += 1
            if possible(i-1, j-1) and l[i-1][j-1] == '#':
                count += 1
            if possible(i+1, j-1) and l[i+1][j-1] == '#':
                count += 1
            l[i][j] = str(count)
for li in l:
    print("".join(li))
