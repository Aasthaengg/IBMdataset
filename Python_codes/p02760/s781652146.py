A = [list(map(int,input().split())) for _ in range(3)]
N = int(input())

bingo = [[0 for _ in range(3)] for _ in range(3)]

for _ in range(N):
  b = int(input())
  for i in range(3):
    for j in range(3):
      if A[i][j] == b:
        bingo[i][j] = 1
        
check = False

for i in range(3):
  if 0 not in bingo[i]:
    check = True
  
for j in range(3):
  if bingo[0][j] + bingo[1][j] + bingo[2][j] == 3:
    check = True
    
if bingo[0][0] + bingo[1][1] + bingo[2][2] == 3:
  check = True

if bingo[0][2] + bingo[1][1] + bingo[2][0] == 3:
  check = True
  
print("Yes" if check else "No")