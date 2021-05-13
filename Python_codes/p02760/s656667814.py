array = [ list(map(int,input().split())) for _ in range(3) ]
number = []
N = int(input())
for _ in range(N):
  number += [ int(input()) ]
for i in range(3):
  for t in range(3):
    if array[i][t] in number:
      array[i][t] = 0
for i in range(1):
  if array[i][0] == array[i+1][0] == array[i+2][0]:
    print('Yes')
    exit()
  elif array[i][1] == array[i+1][1] == array[i+2][1]:
    print('Yes')
    exit()
  elif array[i][2] == array[i+1][2] == array[i+2][2]:
    print('Yes')
    exit()
  elif array[i][0] == array[i][1] == array[i][2]: 
    print('Yes')
    exit()
  elif array[i+1][0] == array[i+1][1] == array[i+1][2]:
    print('Yes')
    exit()
  elif array[i+2][0] == array[i+2][1] == array[i+2][2]:
    print('Yes')
    exit()
    
if array[0][0] == array[1][1] == array[2][2] or array[0][2] == array[1][1] == array[2][0]:
  print('Yes')
else:
  print('No')
