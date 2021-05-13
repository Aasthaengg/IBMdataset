from sys import exit
S = input()
for letter in 'abcdefghijklmnopqrstuvwxyz':
  if letter not in S:
    print(letter)
    exit(0)
print(None)