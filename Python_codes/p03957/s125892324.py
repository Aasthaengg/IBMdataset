S = input()
flag = False
for s in S:
    if s == "C":
        flag = True

    if flag:
        if s == "F":
            print("Yes")
            break
else:
    print("No")
