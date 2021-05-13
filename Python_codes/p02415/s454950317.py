string = input()
out_string = []
for i in range(len(string)):
    if string[i].isupper():
        out_string.append(string[i].lower())
    else:
        out_string.append(string[i].upper())

print("".join(out_string))