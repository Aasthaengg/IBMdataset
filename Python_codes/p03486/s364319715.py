S = list(input())
T = list(input())
s = []
t = []
for i in S:
  s.append(int(ord(i)))
for i in T:
  t.append(int(ord(i)))

s.sort()
t.sort()
for i in range(max(len(s),len(t))):
  if i >= min(len(s),len(t)):
    break
  elif max(t) > s[i]:
    print("Yes")
    exit(0)
  elif s[i] not in t:
    break
  else:
    t.remove(s[i])
    s.remove(s[i])
    
  
if len(t) > len(s):
  for i in s:
    if i not in t:
      print("No")
      exit(0)
    else:
      t.remove(i)
  print("Yes")
else:
  print("No")
 

