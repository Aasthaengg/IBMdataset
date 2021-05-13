strings=input()

for i in strings:
    if "a" <= i <= "z":
        print(i.upper(), end="")
    elif "A" <= i <= "Z":
        print(i.lower(), end="")
    else:
        print(i, end="")
print("")