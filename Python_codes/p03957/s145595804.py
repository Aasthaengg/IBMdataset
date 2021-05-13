s = input()
check1 = False
check2 = False
for i in range(len(s)):
    if s[i] == "C":
        if not check1:
            check1 = True
    if s[i] == "F":
        if check1:
            check2 = True
if check1 and check2:
    print("Yes")
else:
    print("No")