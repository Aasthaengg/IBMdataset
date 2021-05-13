n = int(input())
s = input()
red = 0
blue = 0
for i in range(n):
    if s[i] == "R":
        red += 1
    else:
        blue += 1

if red > blue:
    print("Yes")
else:
    print("No")