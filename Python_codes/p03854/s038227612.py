s=list(input())
ans="YES"
while len(s)!=0:
  if len(s)<5:
    ans="NO"
    break
  elif s[-1:-6:-1]==["m","a","e","r","d"]:
    for i in range(5):
      s.pop(-1)
  elif s[-1:-8:-1]==["r","e","m","a","e","r","d"]:
    for i in range(7):
      s.pop(-1)
  elif s[-1:-6:-1]==["e","s","a","r","e"]:
    for i in range(5):
      s.pop(-1)
  elif s[-1:-7:-1]==["r","e","s","a","r","e"]:
    for i in range(6):
      s.pop(-1)
  else:
    ans="NO"
    break
print(ans)