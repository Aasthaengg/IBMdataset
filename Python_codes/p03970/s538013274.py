S = input()
ref = "CODEFESTIVAL2016"

res = 0
for s, r in zip(S, ref):
  if s != r:
    res += 1
    
print(res)