sx,sy,tx,ty = map(int,input().split())
X = tx - sx
Y = ty - sy
print('R'*X + 'U'*Y + 'L'*X + 'D'*(Y+1) + 'R'*(X+1) + 'U'*(Y+1) + 'LU' + 'L'*(X+1) + 'D'*(Y+1) + 'R')
