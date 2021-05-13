str = input()
cnt = 0
 
for i in range(3):
  if str == 'RRR':
    cnt = 3
  elif str == 'RRS':
    cnt = 2
  elif str == 'SRR':
    cnt = 2
  elif str == 'SSS':
    cnt = 0
  else:
    cnt = 1
    
print(cnt)