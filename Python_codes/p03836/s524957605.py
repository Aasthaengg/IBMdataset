sx,sy,tx,ty = map(int,input().split())
a = tx-sx
b = ty-sy
ans = ''
ans += 'U'*b+'R'*a
ans += 'D'*b+'L'*a
ans += 'L'+'U'*(b+1)+'R'*(a+1)+'D'
ans += 'R'+'D'*(b+1)+'L'*(a+1)+'U'
print(ans)