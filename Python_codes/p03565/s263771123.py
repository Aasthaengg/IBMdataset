S = input().strip()
T = input().strip()
ans = "UNRESTORABLE"
for i in range(len(S)-len(T), -1, -1):
    ok = True
    for j in range(len(T)):
        if not (S[i+j] == '?' or S[i+j] == T[j]):
            ok = False

    if ok:
        ans = S[:i]+T+S[i+len(T):]
        ans = ans.replace("?", "a")
        break
print(ans)
