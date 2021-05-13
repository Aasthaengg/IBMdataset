from collections import Counter

s = input()
t = input()

if sorted(Counter(s).values()) == sorted(Counter(t).values()):
    print("Yes")
else:
    print("No")