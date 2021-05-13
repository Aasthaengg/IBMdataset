sx, sy, tx, ty, = [int(i) for i in input().split()]
x_diff = tx - sx
y_diff = ty - sy

output = ''
# 1周目
output += 'U'*y_diff
output += 'R'*x_diff
output += 'D'*y_diff
output += 'L'*x_diff

#2周目
output += 'L'
output += 'U'*(y_diff+1)
output += 'R'*(x_diff+1)
output += 'D'
output += 'R'
output += 'D'*(y_diff+1)
output += 'L'*(x_diff+1)
output += 'U'

print(output)