s = input()
flag = "off"
for i in s:
    if i == "C":
        flag = "on"
    if flag == "on" and i == "F":
        print("Yes")
        exit()
print("No")