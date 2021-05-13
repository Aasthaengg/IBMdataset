Sd = input()
T = input()


# S'よりTが大きかったら無理
if len(Sd) < len(T):
    print("UNRESTORABLE")
    exit()

head_list = []
# 部分文字列の頭のindex
for i in range(len(Sd) - len(T) + 1):
    sdd = Sd[i:i + len(T)]
    f = True
    for j, sddj in enumerate(sdd):
        if sddj == "?":
            continue
        elif sddj != T[j]:
            f = False
            break
    if f:
        head_list.append(i)

# 候補が見つからなかったら無理
if not head_list:
    print("UNRESTORABLE")
    exit()
else:
    ans_list = []
    for head in head_list:
        ans_list.append((Sd[:head] + T + Sd[head + len(T):]).replace("?", "a"))

    ans_list.sort()
    print(ans_list[0])
