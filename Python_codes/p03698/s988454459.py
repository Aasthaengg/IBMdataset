s = input ()
k = 'yes'
for i in range (len(s)-1):
  if s.count(s[i]) != 1:
    k = 'no'
    break
print (k)