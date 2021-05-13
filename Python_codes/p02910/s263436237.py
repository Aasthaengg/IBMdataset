s = input()
print('Yes' if "L" not in set(s[::2])  and "R" not in set(s[1::2])  else "No")
