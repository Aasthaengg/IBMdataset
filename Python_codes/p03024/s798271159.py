s = list(map(str, input()))
n = s.count("o")
if 15 - len(s) + n >= 8:
    print("YES")
else:
    print("NO")