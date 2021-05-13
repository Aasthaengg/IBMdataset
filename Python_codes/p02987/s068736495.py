from collections import Counter
S = Counter(input())
if len(S) == 2:
    for i in S.values():
        print("No" if i != 2 else "Yes")
        break
else:
    print("No")