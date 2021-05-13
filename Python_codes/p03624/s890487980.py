s = input()
alphabet = 'abcdefghijklmnopqrstuvwxyz'

for i in alphabet:
  if i not in s:
    print(i)
    exit()
print('None')