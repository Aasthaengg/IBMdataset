def main():
  s = input()
  n = len(s)
  x, y = map(int, input().split())

  dpx = [[False, False] for _ in range(n+2)]
  dpy = [[False, False] for _ in range(n+2)]

  dpx[0][0] = True
  dpy[0][0] = True
  x_turn = False
  y_turn = False
  judge = True
  turn = False
  xcount = 0
  count = 0
  for i in range(n):
    if judge and s[i] == "F":
      xcount += 1
      continue
    if judge:
      judge = False
      turn = False if turn else True
      continue
    if s[i] == "F":
      count += 1
      if i != n-1:
        continue
    if turn:
      y_turn = False if y_turn else True
      if y_turn:
        p, q = 0, 1
      else:
        p, q = 1, 0
      for i in range(n+1):
        
        dpy[i][q] = False
      for i in range(n+1):
        if dpy[i][p]:
          dpy[abs(i-count)][q] = True
          dpy[i+count][q] = True
    else:
      x_turn = False if x_turn else True
      if x_turn:
        p, q = 0, 1
      else:
        p, q = 1, 0
      for i in range(n+1):
        dpx[i][q] = False
      for i in range(n+1):
        if dpx[i][p]:
          dpx[abs(i-count)][q] = True
          dpx[i+count][q] = True
    turn = False if turn else True
    count = 0
  
  p = 1 if x_turn else 0
  q = 1 if y_turn else 0
  x -= xcount
  if abs(x) > n:
    print("No")
  elif dpx[abs(x)][p] and dpy[abs(y)][q]:
    print("Yes")
  else:
    print("No")
  
if __name__ == "__main__":
  main()