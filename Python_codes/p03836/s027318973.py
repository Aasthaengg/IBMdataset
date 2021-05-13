sx,sy,tx,ty = map(int,input().split())
U,D,L,R = 'U','D','L','R'
dx,dy = tx-sx,ty-sy
ans = R*dx+U*dy + L*dx+D*(dy+1) + R*(dx+1)+U*(dy+1)+L +U+L*(dx+1)+D*(dy+1)+R
print(ans)