sx, sy, tx, ty = map(int, input().split())

w = tx - sx
h = ty - sy

print('R'*w, end='')
print('U'*h, end='')
print('L'*w, end='')
print('D'*h, end='')
print('D'*1, end='')
print('R'*(w+1), end='')
print('U'*(h+1), end='')
print('L'*1, end='')
print('U'*1, end='')
print('L'*(w+1), end='')
print('D'*(h+1), end='')
print('R'*1, end='')

