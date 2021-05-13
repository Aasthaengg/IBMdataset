O = list(input())
E = list(input())
lo = len(O)
le = len(E)
if lo > le:
  for i in range(le):
    print(O[i]+E[i],end="")
  print(O[-1])
else:
  for i in range(le):
    print(O[i]+E[i],end="")