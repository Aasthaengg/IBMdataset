s = input()
a = s[:2]
b = s[2:]
b1 = 0
a1 = 0

if b[0] == '0': b1 = int(b[1])
else: b1 = int(b)
if a[0] == '0': a1 = int(a[1])
else: a1 = int(a)

if (b1>=1 and b1<=12) and (a1>=1 and a1<=12): print("AMBIGUOUS")
elif b1>=1 and b1<=12: print("YYMM")
elif a1>=1 and a1<=12: print("MMYY")
else: print("NA") 