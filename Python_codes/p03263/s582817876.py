h, w = map(int, input().split())
a = [0]*h
for i in range(h):
  a[i] = [int(x)%2 for x in input().split()]

ans = 0
ans_list = []
key = 0
for i in range(h):
  if i%2 == 0:
    for j in range(w):
      p = a[i][j]
      if key == 0:
        if p == 0:
          pass
        else:
          key = 1
      else:
        if p == 0:
          key = 1
          ans += 1
          if j == 0:
            ans_list.append([i, j+1, i+1, j+1])
          else:
            ans_list.append([i+1, j, i+1, j+1])
        else:
          key = 0
          ans += 1
          if j == 0:
            ans_list.append([i, j+1, i+1, j+1])
          else:
            ans_list.append([i+1, j, i+1, j+1])
        
      
  else:
    for j in range(w-1, -1, -1):
      p = a[i][j]
      if key == 0:
        if p == 0:
          pass
        else:
          key = 1
      else:
        if p == 0:
          key = 1
          ans += 1
          if j == w-1:
            ans_list.append([i, j+1, i+1, j+1])
          else:
            ans_list.append([i+1, j+2, i+1, j+1])
        else:
          key = 0
          ans += 1
          if j == w-1:
            ans_list.append([i, j+1, i+1, j+1])
          else:
            ans_list.append([i+1, j+2, i+1, j+1])

print(ans)
for i in range(ans):
  print(*ans_list[i])