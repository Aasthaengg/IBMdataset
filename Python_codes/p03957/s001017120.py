s = input()
f = 0
for i in s:
    if i == "C" and f == 0:
        f += 1
    if i == "F" and f == 1:
        print("Yes")
        exit()
print("No")