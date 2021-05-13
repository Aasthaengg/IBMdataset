S = input()
T = input()
S_LEN = len(S)
T_LEN = len(T)
ans_li = []
if S_LEN - T_LEN < 0:
    print("UNRESTORABLE")
else:
    for i in range(S_LEN - T_LEN + 1):
        is_ok = True
        for j in range(T_LEN):
            if S[i + j] != "?" and S[i + j] != T[j]:
                is_ok = False
                break
        if is_ok:
            tmp = S[:i] + T + S[i + T_LEN:]
            ans_li.append(tmp.replace("?", "a"))
    print(sorted(ans_li)[0]) if ans_li != [] else print("UNRESTORABLE")
