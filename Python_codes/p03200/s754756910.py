S = input()
k1 = k2 = 0
for i in S[::-1]:
  if i == 'W':
    k2 += 1
  else:
    k1 += k2
print(k1)