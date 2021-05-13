r = input()
n = list(r)
x = int(n[0])*100 + int(n[0])*10 + int(n[0])

if x < int(r):
  print( ((int(n[0])+1)*100 + (int(n[0])+1)*10 + int(n[0])+1))
else:
  print(x)
