s = input()
if len(s) < 8:
    print("YES")
else:
    if s.count('o') + (15 - len(s)) > 7:
        print("YES")
    else:
        print("NO")
