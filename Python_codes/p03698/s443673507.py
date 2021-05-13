def countchar(s) : 
  countstr = [0] * 300
  for i in s : 
    if countstr[ord(i)] != 0 : 
      return False
    countstr[ord(i)] += 1
  return True


s = input()


if countchar(s) : 
  print('yes') 
else : 
  print('no')