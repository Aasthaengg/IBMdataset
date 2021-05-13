S = input()
a = len(S)
count=0
for i in range(a):
  for j in range(i,a):
    XX= S[:i] +S[j:a]
    
    if XX == 'keyence':
      count +=1
if count == 0:
  print('NO')
else:
  print('YES')