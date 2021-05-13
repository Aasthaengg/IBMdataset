s = input()

l = len(s)
d = l - 7

for i in range(7):
    if s[:i] + s[(i + d):] == "keyence":
        print("YES")
        break
    elif i == 6:
        print("NO")