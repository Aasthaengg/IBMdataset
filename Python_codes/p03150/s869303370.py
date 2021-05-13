S = input()

if S[0] != "k":
    if S[-7:] == "keyence":
        print("YES")
    else:
        print("NO")

elif S[-1] != "e":
    if S[:7] == "keyence":
        print("YES")
    else:
        print("NO")

else:
    if S[:1] == "k" and S[-6:] == "eyence":
        print("YES")
    elif S[:2] == "ke" and S[-5:] == "yence":
        print("YES")
    elif S[:3] == "key" and S[-4:] == "ence":
        print("YES")
    elif S[:4] == "keye" and S[-3:] == "nce":
        print("YES")
    elif S[:5] == "keyen" and S[-2:] == "ce":
        print("YES")
    elif S[:6] == "keyenc" and S[-1:] == "e":
        print("YES")
    else:
        print("NO")
