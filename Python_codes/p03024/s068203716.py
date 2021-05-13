s = input()
n = len(s)
if 15 - n + s.count("o") >= 8:
    print("YES")
else:
    print("NO")