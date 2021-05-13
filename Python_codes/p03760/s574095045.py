import sys
o = input ()
e = input ()
for i in range (len(e)):
  sys.stdout.write(o[i])
  sys.stdout.flush()
  sys.stdout.write(e[i])
  sys.stdout.flush()
if len(o) > len(e):
  sys.stdout.write(o[-1])
  sys.stdout.flush()