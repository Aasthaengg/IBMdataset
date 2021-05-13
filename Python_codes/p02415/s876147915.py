string = input()
for n in range(len(string)):
    if string[n] in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        print(string[n].lower(), end="")
    elif string[n] in "abcdefghijkelmnopqrstuvwxyz":
        print(string[n].upper(), end="")
    else:
        print(string[n], end="")
print()