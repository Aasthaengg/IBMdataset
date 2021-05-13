n = int (input ())
l = [int (x) for x in input().split()]
s = sum (l)
m = int (input ())
for i in range (m):
  a,b = map (int, input ().split ())
  print (s-(l[a-1]-b))