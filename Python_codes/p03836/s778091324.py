sx,sy,tx,ty = map(int,input().split())
ans = []

dx = tx - sx
dy = ty - sy
for _ in range(dx):
    ans.append('R')
for _ in range(dy):
    ans.append('U')
for _ in range(dx):
    ans.append('L')
for _ in range(dy):
    ans.append('D')
dx = tx - sx + 1
dy = ty - sy + 1
ans.append('D')
for _ in range(dx):
    ans.append('R')
for _ in range(dy):
    ans.append('U')
ans.append('L')
ans.append('U')
for _ in range(dx):
    ans.append('L')
for _ in range(dy):
    ans.append('D')
ans.append(('R'))
print(''.join(ans))