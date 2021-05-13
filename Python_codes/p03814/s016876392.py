s = input ()
n = len (s)
for i in range (n):
  if s[i] == 'A':
    x = i
    break
for i in range (n):
  if s[-1-i] == 'Z':
    y = n-i-1
    break
print (y-x+1)