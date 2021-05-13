s = input()
flg = False
for ss in s:
    if ss == "C":
        flg = True
    if ss == "F" and flg:
        print("Yes")
        break
else:
    print("No")