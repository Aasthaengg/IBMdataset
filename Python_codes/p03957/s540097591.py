S = input()

c = 0
f = 0
for s in S:
    if s == "C":
        c = 1
    elif c and s == "F":
        f = 1
        break

if c and f:
    print("Yes")
else:
    print("No")