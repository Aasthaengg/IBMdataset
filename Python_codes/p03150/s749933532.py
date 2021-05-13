s = input()
l = len(s) - 7
print("YES" if any(s[:i] + s[i+l:] == "keyence" for i in range(8)) else "NO")