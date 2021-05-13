import re
# ABC162
# Lucky 7
n = input()
m = re.search("7", n)
if m:
    print("Yes")
else:
    print("No")
