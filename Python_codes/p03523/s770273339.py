S = input()
con = "KIHBR"
cnt1 = 0
cnt2 = 0
flag = True
for i in S:
    if cnt1 < 5 and i==con[cnt1]:
        cnt1+=1
        cnt2=0
    elif i=="A":
        if cnt1==1 or cnt1==2:
            flag = False
            break
        cnt2+=1
        if cnt2==2:
            flag = False
            break
    else:
        flag = False
        break
print("YES") if flag and cnt1==5 else print("NO")