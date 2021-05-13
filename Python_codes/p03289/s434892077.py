# coding = SJIS
s = str(input())
lar = "BDEFGHIJKLMNOPQRSTUVWXYZ"
if s[0] != "A":
    print("WA")
    exit()
elif s[2:len(s)-1].count("C") != 1:
    print("WA")
    exit()
elif s[0:2].count("C") + s[-1].count("C") > 0:
    print("WA")
    exit()
kaz = 0
for i in lar:
    kaz += s.count(i)
if kaz > 0:
    print("WA")
    exit()
print("AC")