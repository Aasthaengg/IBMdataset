s = input()
print(["Yes", "No"]["L" in s[::2] or "R" in s[1::2]])