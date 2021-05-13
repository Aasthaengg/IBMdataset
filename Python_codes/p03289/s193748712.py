s = input()

flg = 0

if s[0] == "A":
    flg = 1
else:
    print("WA")
    exit()

t  = s[2:-1]


if t.count("C") == 1:
    flg = 1
else:
    print("WA")
    exit()

s=s.replace("A", "")
s =s.replace("C", "")


if s.islower():
    print("AC")
else:
    print("WA")
