S = input()
T = input()
l = len(S)
f = 0
for i in range(l):
  P = str(S[-1]) + S[:-1]
  if P == T:
    print("Yes")
    f = 1
    break
  S = P
if f == 0:
  print("No")