S = input()
a = b = 0
for i in range(len(S)):
  if S[i]== 'B':
    b += 1
  else:
    a += b
print(a)