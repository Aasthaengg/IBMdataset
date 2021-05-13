sx,sy,tx,ty = map(int,input().split())
going1 = ''
returning1 = ''
going2 = ''
returning2 = '' 
a = tx - sx
b = ty - sy
going1 ='U' * b + 'R' * a
returning1 = 'D' * b + 'L' * a
going2 = 'L' + 'U' * (b + 1) + 'R' * (a + 1) + 'D'
returning2 = 'R' + 'D' * (b + 1) + 'L' * (a + 1) + 'U'
print(going1 + returning1 + going2 + returning2)

