s = input()
flg = 1

for i in range(len(s)):
    cou = s.count(s[i])
    if (cou > 1) :
        flg = 0
        break
if (flg) : print("yes")
else : print("no")