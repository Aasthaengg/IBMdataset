import re
s = input()

s1 = re.fullmatch(r"A([a-z]+)C([a-z]+)", s)

if s1 == None:
    print("WA")
else:
    print("AC")
