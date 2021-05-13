sx, sy, tx, ty = map(int,input().split())

w = tx - sx
h = ty - sy

ans = ['R'*w + 'U'*(h+1) + 'L'*(w+1) + 'D'*(h+1) + 'RD' + 'R'*(w+1) + 'U'*(h+1) + 'L'*(w+1) + 'D'*h]

print(*ans)
