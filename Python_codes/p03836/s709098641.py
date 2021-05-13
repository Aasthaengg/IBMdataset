sx,sy,tx,ty = map(int,input().split())

x_diff = tx-sx
y_diff = ty-sy

up = 'U'*abs(y_diff)
down = 'D'*abs(y_diff)
left = 'L'*abs(x_diff)
right = 'R'*abs(x_diff)

ans = right+up+left+down
ans = ans+'DR'+right+up+'UL'+'UL'+left+down+'DR'

print(ans)