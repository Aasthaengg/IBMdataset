sx, sy, tx, ty = map(int, input().split())
dx = tx - sx
dy = ty - sy
ans = ''
for i in range(dx):
    ans+='R'
for j in range(dy):
    ans+='U'
for i in range(dx):
    ans+='L'
for j in range(dy):
    ans+='D'
ans+='D'
for i in range(dx+1):
    ans+='R'
for j in range(dy+1):
    ans+='U'
ans+='LU'
for i in range(dx+1):
    ans+='L'
for j in range(dy+1):
    ans+='D'
ans+='R'
print(ans)