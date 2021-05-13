from collections import Counter
S = Counter(input())
print("yes" if set(S.values()) == {1} else "no")