S = input().strip()
N = len(S)
if N<5:
    print("NO")
else:
    flag = 0
    cur = N
    while cur>0:
        if cur>=7 and S[cur-7:cur]=="dreamer":
            cur -= 7
        elif cur>=6 and S[cur-6:cur]=="eraser":
            cur -= 6
        elif cur>=5 and S[cur-5:cur] in ["dream","erase"]:
            cur -= 5
        else:
            flag = 1
            break
    if flag==0:
        print("YES")
    else:
        print("NO")