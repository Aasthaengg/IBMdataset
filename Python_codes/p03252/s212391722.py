from collections import Counter

s = list(input())
t = list(input())

cs = Counter(s)
ct = Counter(t)

csv = sorted(cs.values())
ctv = sorted(ct.values())

if csv == ctv:
    print("Yes")
    exit()

print("No")