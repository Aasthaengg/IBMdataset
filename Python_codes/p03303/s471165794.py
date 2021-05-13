S = input()
w = int(input())
s = ''
if w == 1:
  print(S)
else:
  if len(S) % w == 0:
    for i in range(len(S) // w):
      s += S[i * w]
    print(s)
  else:
    for i in range((len(S) // w) + 1):
      s += S[i * w]
    print(s)
