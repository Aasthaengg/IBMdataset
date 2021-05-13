sx,sy,tx,ty = map(int, open(0).read().split())
dx = tx - sx
dy = ty - sy
ans = ['L'] + (['U']*(dy+1)) + (['R']*(dx+1)) + ['D','R'] + (['D']*(dy+1)) + (['L']*(dx+1)) + ['U'] + (['U']*(dy)) + (['R']*(dx)) + (['D']*(dy)) + (['L']*(dx))
print(''.join(ans))