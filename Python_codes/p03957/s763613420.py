s = input()
n = len(s)
yes = False
for i in range(n):
    for j in range(i + 1, n):
        if s[i] == "C" and s[j] == "F":
            yes = True
if yes:
    print("Yes")
else:
    print("No")