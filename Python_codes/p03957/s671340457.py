s = input().strip()
if "C" in s:
    indc = s.index("C")
else:
    indc = 10**3
if "F" in s[indc:]:
    indf = indc+s[indc:].index("F")
else:
    indf = -1
if indc<indf:
    print("Yes")
else:
    print("No")
