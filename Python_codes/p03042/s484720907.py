s = list(input())
a = int("".join(s[:2]))
b = int("".join(s[2:]))
c = 0
d = 0
if a and a <= 12:
    c = 1
if b and b <= 12:
    d = 1
if c and d:
    print("AMBIGUOUS")
elif c:
    print("MMYY")
elif d:
    print("YYMM")
else:
    print("NA")