from sys import stdin
from itertools import combinations_with_replacement

s = stdin.readline().rstrip()
if s == "KIHBR":
    print("YES")
    exit()
li = [0,4,6,8]
lin = list(combinations_with_replacement(li, 4))
for i in lin:
    akiba = ["","K","I","H","","B","","R",""]
    for j in i:
        akiba[j] = "A"
    if "".join(akiba) == s:
        print("YES")
        exit()
print("NO")