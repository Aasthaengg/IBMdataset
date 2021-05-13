s = input()

return_str = ''
for c in s:
  if(c == '?'):
    return_str += 'D'
  else:
    return_str += c
    
print(return_str)