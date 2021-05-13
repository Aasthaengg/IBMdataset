from collections import Counter
S = input()
counter = Counter(S)
if counter["o"] + 15 - len(S) >= 8:
    print("YES")
else:
    print("NO")