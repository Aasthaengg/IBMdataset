s = sorted(input())
t = sorted(input())[::-1]

for n in range(min(len(s)-1,len(t)-1)):
  if ord(s[0])<ord(t[0]):
    print("Yes")
    exit()
  elif ord(s[0])>ord(t[0]):
    print("No")
    exit()
  else:
    s = s[1:]
    t = t[1:]
    
if ord(s[0])<ord(t[0]) :
  print("Yes")
elif ord(s[0])>ord(t[0]):
  print("No")
elif len(s)<len(t):
  print("Yes")
else:
  print("No")