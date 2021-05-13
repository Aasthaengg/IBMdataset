s = list(input())
if "C" in s and "F" in s:
    c_ind = s.index("C")
    if "F" in s[c_ind:]:
        print("Yes")
    else:
        print("No")
else:
    print("No")
