string = input()
 
if string[-1] != 's':
  new_string = string[0:] + 's'
if string[-1] == 's':
  new_string = string[0:] +'es'
 
print(new_string)