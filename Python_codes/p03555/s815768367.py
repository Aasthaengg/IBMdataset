s = input()
t = input()
ok = True
if s[0] != t[2]: ok = False
if s[1] != t[1]: ok = False
if s[2] != t[0]: ok = False
if ok == 1: print("YES")
else: print("NO")