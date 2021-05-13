import re

S = input()
m = re.match(r"^A?KIHA?BA?RA?$", S)
if m:
    print("YES")
else:
    print("NO")

