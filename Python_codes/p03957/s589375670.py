s = input()
flag = 0
for i in range(len(s)):
    if flag == 0 and s[i] == "C":
        flag += 1
    if flag == 1 and s[i] == "F":
        flag += 1
if flag == 2:
    print("Yes")
else:
    print("No")