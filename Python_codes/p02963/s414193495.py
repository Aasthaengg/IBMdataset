S = int(input())
  
X1, Y1 = 0, 0

X2, Y3 = int(S ** (1 / 2)), int(S ** (1 / 2))

if X2 < 10 ** 9:
  X2 += 1
if Y3 < 10 ** 9:
  Y3 += 1
if X2 * Y3 >= S:  
  X3, Y2 = X2 * Y3 - S, 1

print(X1, Y1, X2, Y2, X3, Y3)