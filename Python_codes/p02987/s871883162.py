from collections import Counter

S = list(input())
c = Counter(S)

if len(c) != 2:
    print("No")
else:
    for k, v in c.items():
        if v != 2:
            print("No")
            break
    else:
        print("Yes")
