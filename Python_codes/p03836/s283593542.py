sx,sy,tx,ty=map(int,input().split())
dx=tx-sx
dy=ty-sy
ans=''

ans+='R'*dx
ans+='U'*dy
ans+='L'*dx
ans+='D'*dy
ans+='DR'
ans+='R'*dx
ans+='U'*dy
ans+='ULUL'
ans+='L'*dx
ans+='D'*dy
ans+='DR'

print(ans)