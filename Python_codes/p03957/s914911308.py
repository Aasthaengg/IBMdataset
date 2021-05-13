s = input()

num = 0
flag = False
for i in range(len(s)):
    if s[i] == "C" and num == 0:
        num = 1
    elif s[i] == "F" and num == 1:
        flag = True
        break

if flag:
    print("Yes")
else:
    print("No")