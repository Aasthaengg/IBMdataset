S = input()

xCount = 0
for s in S:
    if s == "x":
        xCount += 1

if xCount >= 8:
    print("NO")
else:
    print("YES")