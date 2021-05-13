h,w = map(int,input().split())

s = [list('.'*(w+2))]
for _ in range(h):
    s.append(list('.'+input()+'.'))
s.append(list('.'*(w+2)))

for i in range(h):
    for j in range(w):
        if s[i+1][j+1] == '#':
            if s[i+2][j+1] == '.' and s[i][j+1] == '.' and s[i+1][j+2] == '.' and s[i+1][j] == '.':
                print('No')
                exit()
print('Yes')