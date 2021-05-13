sx,sy,tx,ty=map(int,input().split())
for i in range(sy,ty):
    print('U',end='')
for i in range(sx,tx):
    print('R',end='')
for i in range(sy,ty):
    print('D',end='')
for i in range(sx,tx):
    print('L',end='')
print('L',end='')
for i in range(sy,ty+1):
    print('U',end='')
for i in range(sx,tx+1):
    print('R',end='')
print('D',end='')
print('R',end='')
for i in range(sy,ty+1):
    print('D',end='')
for i in range(sx,tx+1):
    print('L',end='')
print('U',end='')