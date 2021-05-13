from collections import Counter

S = str(input())

if all(v == 2 for v in Counter(S).values()):
    print("Yes")
else:
    print("No")