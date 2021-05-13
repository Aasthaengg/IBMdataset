n = int (input ())
s = input ()
x = 0
for i in range (n):
  y = s[:i+1].count ('I') - s[:i+1].count ('D')
  if x < y:
    x = y
print (x)