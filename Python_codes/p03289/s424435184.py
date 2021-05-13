s = input()

cond = True

if s[0] != "A":
    cond = False

if s[2:-1].count("C") != 1:
    cond = False

s = s.replace("C", "")
if not s[1:].islower():
    cond = False

print("AC" if cond else "WA")
