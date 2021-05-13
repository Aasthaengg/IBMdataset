#itertoolsを使うversion
import itertools
S = input()
N = len(S)
res = 0
for ptr in itertools.product([0,1], repeat=(N-1)):
  formula = ""
  for i in range(N-1):
    if ptr[i] == 1:
      formula += S[i]
      formula += "+"
    else:
      formula += S[i]
  formula += S[N-1]    
  res += eval(formula)
print(res)