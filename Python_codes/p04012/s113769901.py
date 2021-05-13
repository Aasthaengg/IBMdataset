w = input()
a = set(w)
flg  = 1
for i in a:
    if (w.count(i)%2 != 0) :
        flg = 0
        break

if (flg):print("Yes")
else: print("No")