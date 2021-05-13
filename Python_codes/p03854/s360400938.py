S = list(input())

flag = True
while flag == True:
    if len(S) == 0:
        break
    if len(S) >= 5:
        if S[-5:] == list("dream"): del S[-5:]
        elif S[-5:] == list("erase"): del S[-5:]
        elif len(S)>=6 and S[-6:] == list("eraser"): del S[-6:]
        elif len(S)>=7 and S[-7:] == list("dreamer"): del S[-7:]
        else:
            flag = False
    else:
        flag = False
if flag:
    print("YES")
else:print("NO")