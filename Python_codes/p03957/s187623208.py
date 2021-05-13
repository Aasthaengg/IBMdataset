s = list(input())
c = 0
f = 0
for i in s:
    if i == "C":
        c += 1
    if c == 0:
        continue
    if i == "F":
        print("Yes")
        exit(0)
print("No")
