import sys
a,b = map(str,input().split())
if not a in ("H","D"):
    sys.exit()

if (a == "H" and b == "H") or (a == "D" and b == "D"):
    print("H")
else:
    print("D")