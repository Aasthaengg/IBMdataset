a,b=map(int,input().split())
board=[['.']*100 for _ in range(100)]
pos=0
for i in range(0,(a-1)//50):
  for j in range(0,100,2):
    board[2*i][j+1]='#'
    board[2*i+1][j]='#'
    board[2*i+1][j+1]='#'
pos=2*((a-1)//50)
for j in range(0,2*((a-1)%50),2):
  board[pos][j+1]='#'
  board[pos+1][j]='#'
  board[pos+1][j+1]='#'
pos+=3
for i in range(0,(b-1)//50):
  for j in range(0,100,2):
    board[2*i+pos+1][j+1]='#'
pos+=2*((b-1)//50)
for j in range(0,2*((b-1)%50),2):
  board[pos+1][j+1]='#'
pos+=3
if a==1:
  board[pos+1][1]='#'
print(100,100)
for row in board:
  print(''.join(map(str,row)))