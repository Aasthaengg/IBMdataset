s = input()
mae = int(s[:2])
usiro = int(s[2:])

ym = 0
my = 0

if (1 <= usiro <= 12): ym = 1
if (1 <= mae <= 12): my = 1

if (ym and my): print("AMBIGUOUS")
elif (ym): print("YYMM")
elif (my): print("MMYY")
else: print("NA")

