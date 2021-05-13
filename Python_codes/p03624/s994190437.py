S = input()

a = list('abcdefghijklmnopqrstuvwxyz')

n=[]
for i in a:
  if i not in S:
    n.append(i)
    
if len(n)==0:
  print('None')
  
else:
  print(min(n))