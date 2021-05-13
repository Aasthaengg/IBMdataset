from collections import Counter

f = True
s = Counter(input())
for i in list(s.values()):
    if i % 2 != 0:
        f = False

print("Yes") if f else print("No")