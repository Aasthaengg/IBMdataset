sentence = input()
print(''.join(letter.upper() if letter.islower() else letter.lower() for letter in sentence))
