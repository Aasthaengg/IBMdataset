s = input()
s = sorted(s)
s = set(s)
alpha = 'a'
flg = 0
for i in range(1,27):
    if (alpha not in s):
        flg = 1
        break
    else : alpha = chr(ord(alpha)+1)
if (flg): print(alpha)
else: print("None")
