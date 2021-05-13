s = input()
s = s + "o" * (15 - len(s))

if s.count("o") >= 8:
    print("YES")
else:
    print("NO")