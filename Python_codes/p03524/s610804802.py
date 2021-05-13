from collections import Counter

S = input()
C = Counter(S)

if len(C) == 3:
    c = min(C.values())
else:
    c = 0

for cc in C.values():
    if not (cc == c or cc == c + 1):
        print("NO")
        exit()

print("YES")
