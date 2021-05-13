S = input()
n = len(S) - 1
sumLine = 0
for i in range(2 ** n):
  op = [0] * (n)
  e = ''
  for j in range(n):
    if (i >> j) & 1  :
      e += S[j] + '+'
    else:
      e += S[j]

  sumLine += eval(e+S[-1])
print(sumLine)
