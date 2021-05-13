string = input()
for i in string:
    if i.isupper():
        print(i.lower(), end = "")
    elif i.islower():
        print(i.upper(), end = "")
    else:
        print(i, end = "")
print()