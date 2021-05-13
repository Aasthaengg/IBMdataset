N = int(input())
grids = [[s for s in input()],[s for s in input()]]
MOD = 1000000007

if grids[0][0] == grids[1][0]:
  prv_row_type = 1
  ans = 3
  posx = 1
else:
  prv_row_type = -1
  ans = 6
  posx = 2

while posx < N:
  if grids[0][posx] ==  grids[1][posx]:
    if prv_row_type == 1: ans  *= 2
    else: ans *= 1
    prv_row_type = 1
    posx += 1
  else:
    if prv_row_type == 1: ans *= 2
    else: ans *= 3
    prv_row_type = -1
    posx += 2

print(ans%MOD)