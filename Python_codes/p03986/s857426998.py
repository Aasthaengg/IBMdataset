S = input()
k = 0
l = len(S)
for i in S:
  if i == 'S':
    k += 1
  else:
    if k > 0:
      k -= 1
      l -= 2
print(l)