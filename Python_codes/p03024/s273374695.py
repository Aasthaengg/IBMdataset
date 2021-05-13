s = input()
day = 15 - len(s)
count = s.count("o")
if count + day >= 8:
    print("YES")
else:
    print("NO")