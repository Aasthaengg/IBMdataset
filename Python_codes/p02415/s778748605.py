str = input()
dst = ''
for char in str:
    if char.isupper():
        dst += char.lower()
    elif char.islower():
        dst += char.upper()
    else:
        dst += char
print(dst)