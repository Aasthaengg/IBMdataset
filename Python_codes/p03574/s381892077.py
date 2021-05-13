h, w = map(int, input().split())

ans = []
s=[]
s.insert(0,'.'*(w+2))
for i in range(h):
    s.append('.'+input()+'.')
s.append('.'*(w+2))

for y in range(1,h+1):
    column=[]
    for x in range(1,1+w):
        if s[y][x]=='#':
            column.append('#')
        else:
            column.append(str(s[y-1][x-1:x+2].count('#')+s[y][x-1:x+2].count('#')+s[y+1][x-1:x+2].count('#')))
    ans.append(''.join(column))
for i in ans:
    print(i)
