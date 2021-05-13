s = list(input())
s.sort()
print("No" if (s[0] != 'a') or (s[1] != 'b') or s[2] != 'c' else "Yes")