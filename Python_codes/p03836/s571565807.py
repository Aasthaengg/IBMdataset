sx, sy, tx, ty = map(int, input().split())
diff_x = tx - sx
diff_y = ty - sy
ans = 'U' * diff_y + 'R' * diff_x + 'D' * diff_y + 'L' * diff_x
ans += 'LU' + 'U' * diff_y + 'R' * diff_x + 'RDRD' + 'D' * diff_y + 'L' * diff_x + 'LU'
print(ans)