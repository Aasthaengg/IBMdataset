import re

s = "".join("." if i == "?" else i for i in input())
t = input()

lent = len(t)
mstart = -1
for start in range(len(s) - lent + 1):
    m = re.match(re.compile(s[start:start+lent]), t)    
    if m:
        mstart = start
else:
    if mstart == -1:
        print("UNRESTORABLE")
    else:
        s = s[:mstart] + t + s[mstart+lent:]
        print(s.replace(".", "a"))