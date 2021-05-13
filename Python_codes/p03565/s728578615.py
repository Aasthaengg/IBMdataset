S = input()
T = input()

found = False
res = ""
len_S = len(S)
len_T = len(T)
found = False

for i in range(len_S):
    cnt = 0
    if i == len_S - len_T + 1: break
    for j in range(len_T):
        if T[j] == S[i+j] or S[i+j] == "?":
            cnt+=1
        if cnt == len_T:
            tmps = S[:i]
            tmpt = S[i+len_T:]
            res = S[:i] + T + S[i+len_T:]
            found = True
            break

if found: print(res.replace("?", "a"))
else: print("UNRESTORABLE")