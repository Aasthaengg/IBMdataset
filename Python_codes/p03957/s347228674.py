from sys import stdin

s = stdin.readline().rstrip()
now = 0
for i in s:
    if now == 0 and i == "C":
        now += 1
    elif now == 1 and i == "F":
        print("Yes")
        exit()
print("No")