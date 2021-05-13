letters = list(input())
new_letters = []

for i, ltr in enumerate(letters, 1):
  if i % 2 == 1:
    new_letters.append(ltr)

print(''.join(new_letters))
