s=list(map(int,tuple(input())))
k=int(input())
i=0
if 1 in s:
  for i in range(len(s)):
    if s[i]!=1:
      break
  if i>=k:
      print(1)
  else:
      print(s[i])
else:
  print(s[0])