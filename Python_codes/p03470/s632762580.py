from collections import Counter

N, *D = map(int, open(0).read().split())

print(len(Counter(D).most_common()))