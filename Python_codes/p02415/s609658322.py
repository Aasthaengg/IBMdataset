strings = input()
result = ''

for i in range(len(strings)):
    if strings[i].isupper():
        result += strings[i].lower()
    elif strings[i].islower():
        result += strings[i].upper()
    else:
        result += strings[i]

print(result)
