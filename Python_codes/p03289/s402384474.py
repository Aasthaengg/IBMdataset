import re

s = input()
flg = True
if s[0] != "A":
    flg = False
if s[2:-1].count("C") != 1:
    flg = False
if len(re.findall("[A-Z]", s)) != 2:
    flg = False
print("AC" if flg else "WA")
