A,B = map (int, input ().split ())
p = 0
for i in range (2):
  if A > B:
    p += A
    A -= 1
  else:
    p += B
    B -= 1
print (p)