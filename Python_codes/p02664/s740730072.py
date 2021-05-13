t = list(input())    
for i in range(len(t)):

  if t[i] == '?':
    if len(t) == 1:
      if t[i] == '?':
        t[i] = 'D'
      break
    if i == 0:
      if t[1] == 'P':
        t[i] = 'D'
      else:
        t[i] = 'P'
    if i == len(t)-1:
        t[i] = 'D'
    else:
      if t[i-1] == 'P':
        t[i] = 'D'
      else:
        if t[i+1] == 'P':
          t[i] = 'D'
        else:
          t[i] = 'P'
a = ''
for i in range(len(t)):
  a += t[i]
        
print(a)