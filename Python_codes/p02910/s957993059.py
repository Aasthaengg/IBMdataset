for i,s in enumerate(input(),start=1):
  if i%2==0:
    if s=='R':
      print('No')
      exit(0)
  else:
    if s=='L':
      print('No')
      exit(0)
print('Yes')