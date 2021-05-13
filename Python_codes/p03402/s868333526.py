A, B = map(int, input().split())

h, w = 100, 100
board = [["."] * 100 for i in range(100)]
#print(board)
for i in range(50):
  for j in range(100):
    board[i][j] = "#"
#print(board)

l, r = 0, 0
while A > 1:
  A -= 1
  board[l][r] = "."
  r += 2
  if r == 100:
    l += 2
    r = 0

l, r = 99, 99 
while B > 1:
  B -= 1
  board[l][r] = "#"
  r -= 2
  if r == 1:
    l -= 2
    r = 99
print(h,w)
for i in range(100):
  for j in range(100):
    print(board[i][j], end = "")
  print("")
  
