from collections import Counter

s = input()
c = Counter(s)
print('Yes' if len(c) == 2 and c[s[0]] == 2 else 'No')
