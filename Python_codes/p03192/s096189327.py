import re

N = input()

if "2" in N:
    L = re.findall("2",N)
    print(len(L))
else:
    print("0")
