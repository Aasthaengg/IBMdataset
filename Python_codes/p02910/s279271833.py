s = input()
n = len(s)
yes = True
for i in range(n):
    if i % 2 == 0:
        if s[i] == "L":
            yes = False
    elif s[i] == "R":
        yes = False
if yes:
    print("Yes")
else:
    print("No")