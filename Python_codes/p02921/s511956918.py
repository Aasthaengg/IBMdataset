s = input()
t = input()

if s[0] == t[0] and s[1] == t[1] and s[2] == t[2]:
  print(3)
elif (s[0] == t[0] and s[1] == t[1]) or (s[1] == t[1] and s[2] == t[2]) or (s[2] == t[2] and s[0] == t[0]):
  print(2)
elif s[0] == t[0] or s[1] == t[1] or s[2] == t[2]:
  print(1)
else:
  print(0)