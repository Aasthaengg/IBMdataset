sx,sy,tx,ty = map(int,input().split())
#print(sx,sy,tx,ty)
diffx = tx-sx
diffy = ty-sy
#print(diffx,diffy)
st = ''
for i in range(2):
    if i == 0:
        st = st + 'U'*diffy+'R'*diffx+'D'*diffy+'L'*diffx
    if i ==1:
        st = st + 'L'+'U'*(diffy+1)+'R'*(diffx+1)+'D'+'R'+'D'*(diffy+1)+'L'*(diffx+1)+'U'
print(st)