import sys
sx,sy,tx,ty = map(int,input().split())

if not ( -1000 <= sx <= 1000 and sx < tx <= 1000 ): sys.exit()
if not ( -1000 <= sy <= 1000 and sy < ty <= 1000 ): sys.exit()
if not ( isinstance(sx,int) and isinstance(sy,int) and isinstance(tx,int) and isinstance(ty,int)): sys.exit()

x=tx-sx
y=ty-sy
print('U'*y+'R'*x+'D'*y+'L'*x+'L'+'U'*(y+1)+'R'*(x+1)+'DR'+'D'*(y+1)+'L'*(x+1)+'U')