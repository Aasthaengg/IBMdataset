sx, sy, tx, ty = list(map(int, input().split()))

dx = tx - sx
dy = ty - sy
d1 = ['U']*dy + ['R']*dx
d2 = ['D']*dy + ['L']*dx
d3 = ['L'] + ['U']*(dy+1) + ['R']*(dx+1) + ['D']
d4 = ['R'] + ['D']*(dy+1) + ['L']*(dx+1) + ['U']

print(''.join(d1+d2+d3+d4))
