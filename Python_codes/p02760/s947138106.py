import sys
bin = []

for i in range(3):
  lst = list(map(int,input().split()))
  bin.append(lst)
  
n = int(input())
for i in range(n):
  m = int(input())
  for j in range(3):
    for k in range(3):
      if m == bin[j][k]:
        bin[j][k] = 't'
        break
    
    
for i in range(3):
  if bin[i][0] == 't' and bin[i][1] == 't' and bin[i][2] == 't':
    print('Yes')
    sys.exit()
    
for j in range(3):
  if bin[0][j] == 't' and bin[1][j] == 't' and bin[2][j] == 't':
    print('Yes')
    sys.exit()
    
if (bin[0][0] == 't' and bin[1][1] == 't' and bin[2][2] == 't') or (bin[0][2] == 't' and bin[1][1] == 't' and bin[2][0] == 't'):  
  print('Yes')
  sys.exit()
  
print('No')  


