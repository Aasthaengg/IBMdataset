from collections import Counter
s = Counter(input())
print(2*min(s['0'],s['1']))