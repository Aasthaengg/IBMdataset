from collections import Counter

S = input()

if len(set(S)) == 1:
    print("YES" if len(S) == 1 else "NO")
elif len(set(S)) == 2:
    print("YES" if len(S) <= 2 else "NO")
else:
    c = Counter(S)
    print("YES" if max(c["a"], c["b"], c["c"]) - min(c["a"], c["b"], c["c"]) <= 1 else "NO")