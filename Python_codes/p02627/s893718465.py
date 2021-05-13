import re

n = input()

flag = re.match(r"[a-z]",n)
if flag != None:
    print("a")
else:
    print("A")