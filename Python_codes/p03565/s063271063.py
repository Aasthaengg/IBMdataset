S = input()
T = input()
sl = len(S)
tl = len(T)
ans = "z" * 100
for i in range(sl-tl+1):
    if S[i] == T[0] or S[i] == '?':
        bf = True
        for j in range(tl):
            if S[i+j] != T[j] and S[i+j] != '?':
                bf = False
                break
        if bf:
            new = S[:i] + T + S[i+tl:]
            new = new.replace("?", "a")
            ans = min(ans, new)
if ans == "z" * 100:
    print("UNRESTORABLE")
else:
    print(ans)