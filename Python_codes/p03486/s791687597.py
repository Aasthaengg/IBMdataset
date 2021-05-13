s = input()
t = input()
import sys
if s==t:
    print("No")
    sys.exit()
ss = sorted(list(s))
tt = sorted(list(t))[::-1]
if sorted([ss,tt])[0] == ss:
    print("Yes")
else:
    print("No")