s=input()

if s==s[::-1]:
  if s[:(len(s)-1)//2] == s[:(len(s)-1)//2:-1]:
    ss=s[(len(s)+3)//2-1:len(s)]
    if ss ==  ss[::-1]:
      print('Yes')
    else:
      print('No')
  else:
    print('No')
else:
  print('No')