import re
s = input()
if re.search(r".*C.*F.*", s):
    print("Yes")
else:
    print("No")
