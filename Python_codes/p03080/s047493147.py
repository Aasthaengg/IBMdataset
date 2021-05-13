N = int(input())
s = list(input())


r = 0
b = 0
for c in s:
    if c == "B":
        b += 1
    else:
        r += 1
if b < r:
    print("Yes")
else:
    print("No")
