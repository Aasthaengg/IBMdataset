s=input()

s=s[:len(s)-1]
l=len(s)
if l%2==0:
  for i in range(0,l+1,2):
    x=s[:l-i]
    if x[:len(x)//2] == x[len(x)//2:]:
      print(len(x))
      exit()
else:
  s=s[:len(s)-1]
  l=len(s)
  for i in range(0,l+1,2):
    x=s[:l-i]
    if x[:len(x)//2] == x[len(x)//2:]:
      print(len(x))
      exit()
