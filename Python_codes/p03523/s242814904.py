import re
s = input()
check = "A?KIHA?BA?RA?"
ok = re.fullmatch(check,s)
if ok:
    print("YES")
else:
    print("NO")