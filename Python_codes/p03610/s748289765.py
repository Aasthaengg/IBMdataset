import sys
s = list (input ())
t = (s[::2])
for i in range (len(t)):
  sys.stdout.write(t[i])
  sys.stdout.flush()
