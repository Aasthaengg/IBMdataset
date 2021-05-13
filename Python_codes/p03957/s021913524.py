s = list(input())

f = False
for ss in s:
    if f:
        if ss == "F":
            print("Yes")
            import sys
            sys.exit()
    if ss == "C":
        f = True

print("No")