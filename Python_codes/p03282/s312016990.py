s = list(input())
s = [int(l) for l in s]
k = int(input())

if s[0] > 1:
  print(s[0])
elif sum(s[0:k]) == k and len(s[0:k]) == k:
  print(1)
else:
  i = 0
  while s[i] == 1:
    i += 1
    if s[i] != 1:
      print(s[i])
      break