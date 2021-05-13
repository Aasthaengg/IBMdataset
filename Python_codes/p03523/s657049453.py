import re

s = input()
c = r'A?KIHA?BA?RA?$'
if re.match(c,s):
    print("YES")
else:
    print("NO")