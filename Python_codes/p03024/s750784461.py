s = input()
o = s.count("o")
x = s.count("x")
rest = 15 - o - x
if o + rest >= 8:
    print("YES")
else:
    print("NO")