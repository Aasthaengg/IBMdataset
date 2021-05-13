a = input()

flag = True
c = False

for i in range(len(a)):
    if i == 0 and a[i] != 'A':
        flag = False
        break
    elif i != 0:
        if not c:
            if a[i] == "C":
                if i == 1 or i == len(a)-1:
                    flag = False
                    break
                else:
                    c = True
            elif not a[i].islower():
                flag = False
                break
        else:
            if not a[i].islower():
                flag = False
                break


if flag and c:
    print("AC")
else:
    print("WA")