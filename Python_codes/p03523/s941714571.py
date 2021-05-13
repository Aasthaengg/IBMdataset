#A問題
S=list(str(input()))
aflag = 0
kflag = 0
flag = 0
for s in S:
    if s == "A":
        if aflag == 0:
            aflag = 1
            pass
        else:
            flag = 1
            break
    else:
        if s == "K":
            if kflag == 0:
                aflag = 1
                kflag+=1
            else:
                flag = 1
                break
        elif s == "I":
            if kflag == 1:
                kflag+=1
            else:
                flag = 1
                break
        elif s == "H":
            if kflag == 2:
                kflag+=1
                aflag = 0
            else:
                flag = 1
                break
        elif s == "B":
            if kflag == 3:
                kflag+=1
                aflag = 0
            else:
                flag = 1
                break
        elif s == "R":
            if kflag == 4:
                kflag+=1
                aflag = 0
            else:
                flag = 1
                break
        else:
            flag = 1
            break

if flag == 0 and kflag == 5:
    print("YES")
else:
    print("NO")