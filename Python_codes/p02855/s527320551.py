import sys
sys.setrecursionlimit(10**5)
def solve(cake, start, end, n): #end is not included
  s_1 = None
  s_2 = None
  y = start[0]
  while y < end[0] and (not s_1 or not s_2):
    x = start[1]
    while x < end[1] and (not s_1 or not s_2):
      if cake[y][x] == "#":
        if not s_1:
          s_1 = (y, x)
        elif not s_2:
          s_2 = (y, x)
      x += 1
    y += 1
  rtn = 0
  if s_2:
    if s_1[0] != s_2[0]:
      rtn = solve(cake, (s_2[0], start[1]), end, solve(cake, start, (s_2[0], end[1]), n))
    else:
      rtn = solve(cake, (start[0], s_2[1]), end, solve(cake, start, (end[0], s_2[1]), n))
  else:
    y = start[0]
    while y < end[0]:
      x = start[1]
      while x < end[1]:
        cake[y][x] = n
        x += 1
      y += 1
    rtn = n+1
  return rtn
      
H, W, K = map(int, input().split())
C = [list(input()) for _ in range(H)]
k = solve(C, (0, 0), (H, W), 1)
print("\n".join([" ".join([str(x) for x in c]) for c in C]))