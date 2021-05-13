s = input()

alphabet_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

for i in range(len(s)):
  if s[i] in alphabet_list:
    try:
      alphabet_list.remove(s[i])
    except ValueError:
      continue

if alphabet_list:
  print(alphabet_list[0])
else:
  print('None')