S = input()
N = len(S)
for i in range(N):
    if (i + 1) % 2 == 1:
        if S[i] in ("R", "U", "D"):
            continue
        else:
            print("No")
            exit()
    else:
        if S[i] in ("L", "U", "D"):
            continue
        else:
            print("No")
            exit()
print("Yes")
