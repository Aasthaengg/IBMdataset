k = int(input())
s = list(input())

l=[]
if(len(s)<=k):
  word = "".join(s)
  print(word)
else:
  for i in range(k):
    l.append(s[i])
    name = "".join(l)

  print(name + "...")