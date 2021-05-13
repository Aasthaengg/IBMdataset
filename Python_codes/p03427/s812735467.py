n=int(input())
if n<=9:
  print(n)
else:
  n=str(n)
  x=n[0]
  x=int(x)-1
  if n[1:].count('9')==len(n)-1:
    print(x+1+(len(n)-1)*9)
  else:
    print(x+(len(n)-1)*9)
