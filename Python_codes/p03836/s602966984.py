sx,sy,tx,ty=map(int,input().split())
x=tx-sx
y=ty-sy
if y>0:
    p,r='U','D'
else:
    p,r='D','U'
if x>0:
    q,s='R','L'
else:
    q,s='L','R'
l=[p]*y+[q]*x+[r]*y+[s]*x+[s]+[p]*(y+1)+[q]*(x+1)+[r]+[q]+[r]*(y+1)+[s]*(x+1)+[p]
print(''.join(l))