char = list(input())
for i in range(len(char)):
    if char[i].islower():
        char[i] = char[i].upper()
    elif char[i].isupper():
        char[i] = char[i].lower()
print(''.join(char))
