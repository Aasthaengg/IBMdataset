sx, sy, tx, ty = map(int, input().split())
dx, dy = tx - sx, ty - sy
st = 'U'*dy + 'R'*dx 
ts = 'D'*dy + 'L'*dx
print(st + ts + 'LU'+st+'RD' + 'RD'+ts+'LU')