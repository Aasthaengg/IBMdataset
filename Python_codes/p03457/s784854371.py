N = int(input())
t_x_y = [list(map(int, input().split())) for _ in range(N)]
t_x_y.insert(0, [0, 0, 0])
 
ans = 'Yes'
for i in range(N):
  dt = t_x_y[i+1][0] - t_x_y[i][0]
  dist = abs(t_x_y[i+1][1] - t_x_y[i][1]) + abs(t_x_y[i+1][2] - t_x_y[i][2])
  
  # dt < dist が必要
  if dt < dist:
    ans = 'No'
    break
  else:
    # dt >= dist の上で、dtとdistの偶奇が一致すればよい
    if (dt - dist) % 2 != 0:
      ans = 'No'
      break
  
print(ans)