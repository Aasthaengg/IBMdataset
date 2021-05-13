S = input()
T = input()

from collections import Counter

S_sorted = sorted(Counter(S).values(), reverse = True)
T_sorted = sorted(Counter(T).values(), reverse = True)

if S_sorted == T_sorted:
    print("Yes")
else:
    print("No")