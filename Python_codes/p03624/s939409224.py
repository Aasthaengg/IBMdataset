S = input()
alpha = [chr(ord('a') + i) for i in range(26)]

for letter in alpha:
  if not letter in S:
    print(letter)
    exit()
print('None')