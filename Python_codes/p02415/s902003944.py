str = list(input())
for i in range(len(str)):
    if str[i].islower():
        str[i] = str[i].upper()
    elif str[i].isupper():
        str[i] = str[i].lower()
for i in range(len(str)):
    print(str[i], end = '')
print()
