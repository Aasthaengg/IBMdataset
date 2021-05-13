S = input ()
x = 0
for i in range (len(S)):
  if S[i] == 'C':
    x = 1
    break
if x == 1:
  for j in range (len(S)-i):
    if S[j+i] == 'F':
      x = 2
      break
if x == 2:
  print ('Yes')
else:
  print ('No')