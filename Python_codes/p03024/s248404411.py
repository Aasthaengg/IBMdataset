s = input()
k = len(s)
if 15-k >= 8 - s.count("o"):
    print("YES")
else:
    print("NO")