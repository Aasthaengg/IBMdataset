s = list(input())

flag = True

for i in range(len(s)):
    if i % 2 == 0:
        if s[i] == "L":
            flag = False
            break
    else:
        if s[i] == "R":
            flag = False
            break

if flag:
    print("Yes")
else:
    print("No")

