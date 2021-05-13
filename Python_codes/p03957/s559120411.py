import sys
S = input()


if S.count("C") != 0 and S.count("F") != 0:
    pass
else:
    print("No")
    sys.exit()

ans = 0
for i in range(len(S)):
    if S[i] == "C":
        if S[i:len(S)].count("F") != 0:
            print("Yes")
            sys.exit()

print("No")