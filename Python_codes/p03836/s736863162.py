sx, sy, tx, ty = map(int, input().split())

del_x = tx - sx
del_y = ty - sy
ans = 'U' * del_y + 'R' * del_x + 'D' * del_y + 'L' * (del_x + 1)
ans += 'U' * (del_y + 1) + 'R' * (del_x + 1) + 'DR' + 'D' * (del_y + 1) + 'L' * (del_x + 1) + 'U'
print(ans)