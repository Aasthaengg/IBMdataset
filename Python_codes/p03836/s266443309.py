sx,sy,tx,ty=map(int,input().split())

if tx > sx and ty > sy:mode=0
elif tx > sx and ty < sy:mode=1
elif tx < sx and ty > sy:mode=3
else: mode=2
  
directions=[('R','U'),('R','D'),('L','D'),('L','U'),('R','U'),('R','D'),('L','D'),('L','U')]

ans=[]
d_go,d_re = directions[mode],directions[mode+2]
dx,dy=abs(tx-sx),abs(ty-sy)
go1 = dx*d_go[0] + dy*d_go[1]
re1 = dx*d_re[0] + dy*d_re[1]
go2 = d_re[1]+(dx+1)*d_go[0] + (dy+1)*d_go[1] + d_re[0]
re2 = d_go[1]+(dx+1)*d_re[0] + (dy+1)*d_re[1] + d_go[0]

ans.extend(go1)
ans.extend(re1)
ans.extend(go2)
ans.extend(re2)

print(''.join(ans))