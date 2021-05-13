S = input()

# YYMM
flag1 = False
# MMYY
flag2 = False

if 0 <= int(S[:2]) <= 99 and 1 <= int(S[2:]) <= 12:
    flag1 = True

if 1 <= int(S[:2]) <= 12 and 0 <= int(S[2:]) <= 99:
    flag2 = True

if flag1 and not flag2:
    print("YYMM")
elif not flag1 and flag2:
    print("MMYY")
elif flag1 and flag2:
    print("AMBIGUOUS")
else:
    print("NA")
