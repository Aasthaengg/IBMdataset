s = list(input())
x = 0

for c in s:
    if c == "C":
        x = 1
    elif c == "F" and x == 1:
        print("Yes")
        exit()

print("No")