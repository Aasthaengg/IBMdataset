import sys

line = sys.stdin.readline().replace('\n', '').split(' ')
cnt = 0

height = int(line[1])
width = int(line[2])

for i in range(int(line[0])):

  board = sys.stdin.readline().replace('\n', '').split(' ')
  if int(board[0]) - height >= 0 and int(board[1]) - width >= 0:
    cnt += 1 

  #print (board[0])
print (cnt)