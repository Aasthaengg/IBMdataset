before = input()
after = ''
for letter in before:
    if letter.isupper():
        after += letter.lower()
    elif letter.islower():
        after += letter.upper()
    else:
        after += letter
print(after)