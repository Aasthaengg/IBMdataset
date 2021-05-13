import collections
h, w = map(int, input().split())
maze = [list(input()) for _ in range(h)]
group = [[-1 for _ in range(w)] for _ in range(h)]
group_positions = []
for h_i in range(h):
    for w_i in range(w):
      if maze[h_i][w_i] == ".":
        maze[h_i][w_i] = 0
      else:
        maze[h_i][w_i] = 1
      
def do_append(point, y_diff, x_diff):
  new_x = point[1] + x_diff
  new_y = point[0] + y_diff
  new_color = ((point[2]+1)%2)
  if new_x == -1 or new_x == w or new_y == -1 or new_y == h or new_color != maze[new_y][new_x]:
    return False, False
  elif group[new_y][new_x] != -1:
    return False, False
  else:
    return True, (new_y, new_x, new_color)

def wfs(pos, group_num):
  y_pos = pos[0]
  x_pos = pos[1]
  color = maze[y_pos][x_pos] # 0 white 1 black
  group_positions.append([(y_pos, x_pos, color)])
  
  que = collections.deque()
  que.append((y_pos, x_pos, color))
  group[y_pos][x_pos] = group_num
  while len(que) > 0:
    point = que.popleft()
    for dy in (-1, 0, 1):
      for dx in (-1, 0 , 1):
        if dx * dy != 0:
          continue
        result, new_point = do_append(point, dy, dx)
        if result:
          group[new_point[0]][new_point[1]] = group_num
          group_positions[group_num].append(new_point)
          que.append(new_point)
      
if __name__ == "__main__":
  count = 0
  group_num = 0
  for h_i in range(h):
    for w_i in range(w):
      if group[h_i][w_i] == -1:
        pos = (h_i, w_i)
        wfs(pos, group_num)
        group_num += 1
  
  for g in group_positions:
    black_num = 0
    white_num = 0
    for point in g:
      if point[2] == 0:
        white_num += 1
      else:
        black_num += 1
    count += white_num * black_num
  print(count)