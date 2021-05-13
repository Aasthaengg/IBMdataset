s = input()
a = 0
b = 0

if s[2] == '0': b = int(s[3])
else: b = int(s[2:])
if s[0] == '0': a = int(s[1])
else: a = int(s[:2])

if (b>=1 and b<=12) and (a>=1 and a<=12): print("AMBIGUOUS")
elif b>=1 and b<=12: print("YYMM")
elif a>=1 and a<=12: print("MMYY")
else: print("NA") 