H, W = map(int, input().split())

l = []
for i in range(H):
    l.append(list(input()))

for i in range(H):
    for j in range(W):
        if l[i][j] == '.':
            pass
        elif 0<i and l[i-1][j] == '#':
            pass
        elif 0<j and l[i][j-1] == '#':
            pass
        elif j<W-1 and l[i][j+1] == '#':
            pass
        elif i<H-1 and l[i+1][j] == '#':
            pass
        else:
            print('No')
            exit()
print('Yes')