n = int(input())
p = [list(map(int, input().split())) for _ in range(n)]
ans = 'Yes'
t_diff = 0
x_diff = 0
y_diff = 0
for i in p:
  t_diff = i[0] - t_diff
  x_diff = abs(i[1] - x_diff)
  y_diff = abs(i[2] - y_diff)
  if t_diff >= x_diff + y_diff:
    if (t_diff - x_diff - y_diff)%2 != 0:
      ans = 'No'
      break
  else:
    ans = 'No'
    break
print(ans)