s = input()
flg = 1
if (s[0] != 'A'):
    flg = 0
cnt = 0
for i in s[2:-1]:
    if (i == 'C'): cnt+= 1
if (cnt != 1):
    flg = 0 

cap = 0
for i in s:
    if ('A' <= i <= 'Z'): cap += 1
if (cap != 2):
    flg = 0
if (flg): print("AC")
else: print("WA")