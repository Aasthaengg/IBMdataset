line = raw_input()
output = ""
for i in line:
    if i.isupper():
        output += i.lower()
    elif i.islower():
        output += i.upper()
    else:
        output += i
print output