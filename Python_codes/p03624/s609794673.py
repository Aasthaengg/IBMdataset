import string
S = list(input())
ar = string.ascii_lowercase
for w in ar:
  if w not in S:
    print(w)
    exit()
print('None')