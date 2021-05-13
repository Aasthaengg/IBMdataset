import re

S = input()
if re.findall("s+$", S)== ["s"]:
    print(S+"es")
else:
    print(S+"s")