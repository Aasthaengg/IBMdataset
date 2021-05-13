sx, sy, tx, ty = map(int, input().split())

move = ''
xz = abs(tx-sx)
yz = abs(ty-sy)
move += 'U'*yz + 'R'*xz + 'D'*yz + 'L'*xz
move += 'L'*1 + 'U'*(yz+1) + 'R'*(xz+1) + 'D'*1
move += 'R'*1 + 'D'*(yz+1) + 'L'*(xz+1) + 'U'*1
print(move)