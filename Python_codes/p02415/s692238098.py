strings = input()
for character in strings:
    if character.isupper():
        print(character.lower(), end="")
    else:
        print(character.upper(), end="")
print()
