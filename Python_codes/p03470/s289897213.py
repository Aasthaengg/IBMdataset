N = input()
d = []
try :
  while True:
    a = input()
    if a :
      d.append(a)
    else :
      break
except EOFError:
  pass
c = 0
import copy
e = copy.copy(d)
for i in e :
  x = d.pop(0)
  if x not in d: 
    c += 1
print(c)