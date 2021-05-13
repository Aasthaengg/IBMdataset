S = str(input())

if S[:7] == "keyence" or S[-7:] == "keyence":
    print("YES")
    exit()

elif S[:1] + S[-6:] == "keyence" or S[:2] + S[-5:] == "keyence" or S[:3] + S[-4:] == "keyence" or S[:4] + S[-3:] == "keyence" or S[:5] + S[-2:] == "keyence" or S[:6] + S[-1:] == "keyence":
    print("YES")
    exit()

else:
    print("NO")
