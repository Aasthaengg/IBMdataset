N = int (input ())
l = [int(x) for x in input ().split ()]
m = max (l)
s = sum (l)
if m*2 < s:
  print ('Yes')
else:
  print ('No')