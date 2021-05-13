import string

s = set(input())
alphabets = set(string.ascii_lowercase)

l = sorted(list(alphabets - s))

if len(l) == 0:
  print('None')
else:
  print(l[0])