from sys import stdin

s = stdin.readline().rstrip()
point = 0
for i in s:
    if i == "x":
        point += 1
if point >= 8:
    print("NO")
else:
    print("YES")