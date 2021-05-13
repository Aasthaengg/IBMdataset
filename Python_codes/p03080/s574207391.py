N = int(input())
s = list(input())
r, b = 0, 0
for i in s:
    if i == "R":
        r += 1
    else:
        b += 1
if r > b:
    print('Yes')
else:
    print("No")