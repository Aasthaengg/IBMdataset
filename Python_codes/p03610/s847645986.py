s = list(str(input()))

l = []
for i in range(len(s)):
  if i%2 == 0:
    l.append(s[i])

print(''.join(l))
