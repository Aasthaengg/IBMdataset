s = input()
diff = 0
for i in range(len(s)):
    if i % 2 == 0:
        if s[i] == "R" or s[i] == "U" or s[i] == "D":
            continue
        else:
            diff += 1
    if i % 2 == 1:
        if s[i] == "L" or s[i] == "U" or s[i] == "D":
            continue
        else:
            diff += 1
if diff == 0:
    print("Yes")
else:
    print("No")