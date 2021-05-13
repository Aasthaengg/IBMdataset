from collections import Counter

s = input()
counter = Counter(s)
if len(counter.keys()) == 2:
    for key, val in counter.items():
        if val != 2:
            print("No")
            exit()
    print("Yes")
else:
    print("No")
