sx,sy,tx,ty = map(int,input().split())
going1 = ''
returning1 = ''
going2 = ''
returning2 = ''
going1 = 'R' * (tx - sx) + 'U' * (ty - sy)
returning1 = 'L' * (tx -sx) + 'D' * (ty - sy)
going2 = 'D' + 'R' * (tx - sx + 1) + 'U' * (ty - sy + 1) + 'L'
returning2 = 'U' + 'L' * (tx - sx + 1) + 'D' * (ty - sy + 1) + 'R' 
print(going1 + returning1 + going2 + returning2)
