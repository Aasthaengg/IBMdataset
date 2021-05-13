letters = input()
for letter in letters:
    if letter.islower():
        print(letter.upper(), end='')
    elif letter.isupper():
        print(letter.lower(), end='')
    else:
        print(letter, end ='')
print('')