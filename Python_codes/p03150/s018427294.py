S = input()

res = "NO"
if S == "keyence":
    res = "YES"
else:
    if "keyence" in S:
        if S[:7] == "keyence" or S[-7:] == "keyence":
            res = "YES"
    else:
        if S[0] == "k" and S[-6:] == "eyence":
            res = "YES"
        elif S[:2] == "ke" and S[-5:] == "yence":
            res = "YES"
        elif S[:3] == "key" and S[-4:] == "ence":
            res = "YES"
        elif S[:4] == "keye" and S[-3:] == "nce":
            res = "YES"
        elif S[:5] == "keyen" and S[-2:] == "ce":
            res = "YES"
        elif S[:6] == "keyenc" and S[-1:] == "e":
            res = "YES"

print(res)