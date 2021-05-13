sx, sy, tx, ty = map(int,input().split())
Way = [''] * 4 
Way[0] = 'R' * (tx-sx) + 'U' * (ty-sy)
Way[1] = 'L' * (tx-sx) + 'D' * (ty-sy)
Way[2] = 'D' + 'R' * (tx-sx+1) + 'U' * (ty-sy+1) + 'L'
Way[3] = 'U' + 'L' * (tx-sx+1) + 'D' * (ty-sy+1) + 'R'
print(''.join(Way))