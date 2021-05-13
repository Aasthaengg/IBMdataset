N = int (input ())
S = input ()
x = 0
for i in range (N-1):
  L = S[:i+1]
  R = S[i+1:]
  X = 0
  for i in range (len(L)):
    if R.count(L[i]) != 0 and L[:i].count(L[i]) == 0:
      X += 1
  if X > x:
    x = X
print (x)