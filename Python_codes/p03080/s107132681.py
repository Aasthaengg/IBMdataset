n = int(input())
s = input()

r = 0
b = 0
for i in s:
    if i == "R":
        r += 1
    else:
        b += 1

if r > b:
    print("Yes")
else:
    print("No")
