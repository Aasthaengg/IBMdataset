S_p = input()
T = input()
S_len = len(S_p)
T_len = len(T)

if S_len < T_len:
    print("UNRESTORABLE")
    exit(0)

ans = []
for offset in range(S_len - T_len + 1):
    isRestorable = True
    for d in range(T_len):
        if S_p[offset+d] == "?":
            continue
        elif S_p[offset+d] != T[d]:
            isRestorable = False
            break
        else:
            pass
    if isRestorable:
        tmp = S_p[:offset] + T + S_p[offset+T_len:]
        ans.append(tmp.replace("?", "a"))
if len(ans) == 0:
    print("UNRESTORABLE")
else:
    ans.sort()
    print(ans[0])
