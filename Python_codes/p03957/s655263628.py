s=input()
print("Yes" if "C" in s and "F" in s[s.index("C"):] else "No")