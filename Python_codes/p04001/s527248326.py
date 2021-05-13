#bit使うversion
S = input()
N = len(S)
res = 0
for i in range(2**(N-1)):
  formula = ""
  for j in range(N-1):
    if (i>>j) & 1: 
      formula += S[j]
      formula += "+"
    else:
      formula += S[j]
  formula += S[N-1]
  res += eval(formula)
print(res)  