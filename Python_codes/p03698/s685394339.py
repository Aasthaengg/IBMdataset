S = input()
A = [0 for i in range(26)]
f = 0
for i in range(len(S)):
  a = ord(S[i]) - 97
  if A[a] != 0:
    print("no")
    f = 1
    break
  else:
    A[a] = 1
if f == 0:
  print("yes")