a,b=map(int,input().split())
for i,s in enumerate(input()):
  if i == b-1:
    s = chr(ord(s)+32)
  print(s,sep='',end='')