s = input()
print("Yes" if any([s[i:i + 2] == "AC" for i in range(len(s) - 1)]) else "No")