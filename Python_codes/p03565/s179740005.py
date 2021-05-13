import re

s = "".join("." if i == "?" else i for i in input())
t = input()

lent = len(t)
mgroup = ""
mstart = 0
for start in range(len(s) - lent + 1):
    m = re.match(re.compile(s[start:start+lent]), t)    
    if m:
        mgroup, mstart = m.group(), start
else:
    if mgroup:
        s = s[:mstart] + t + s[mstart+lent:]
        print(s.replace(".", "a"))
    else:
        print("UNRESTORABLE")