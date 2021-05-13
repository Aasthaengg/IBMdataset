s = input()

if len(s) < 5:
    print("NO")
    exit()

for i in range(0, 9, 2):
    if i == 8 and len(s) <= 8:
        s = s[:i] + "A" + s[i:]
    elif i != 2:
        if s[i] != "A":
            s = s[:i] + "A" + s[i:]
if s == "AKIHABARA":
    print("YES")
else:
    print("NO")