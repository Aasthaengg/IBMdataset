s = input()
print("Yes" if s[0] == s[1] != s[2] == s[3] or s[0] == s[2] != s[1] == s[3] or s[0] == s[3] != s[2] == s[1] else "No")