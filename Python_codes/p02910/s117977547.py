S = str(input())
 
Ans = True
for i in range(0, len(S)):
  if (i + 1) % 2 == 0:
    if S[i] != 'L' and S[i] != 'U' and S[i] != 'D':
      Ans = False
      break
  if (i + 1) % 2 == 1:
    if S[i] != 'R' and S[i] != 'U' and S[i] != 'D':
      Ans = False
      break
  
if Ans == False:
  print('No')
else:
  print('Yes')