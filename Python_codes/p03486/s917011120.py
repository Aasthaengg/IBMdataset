#-------------
s = input()
t = input()
#-------------
s = list(s)
t = list(t)

s.sort()
t.sort(reverse = True)

if t > s :
  print("Yes")
else :
  print("No")