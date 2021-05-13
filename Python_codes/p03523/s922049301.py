import re
s = input()
m = re.fullmatch("A?KIHA?BA?RA?",s)
if m:
    print("YES")
else:
    print("NO")