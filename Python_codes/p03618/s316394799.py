from collections import Counter

a = input()

n_all_pairs = (len(a)*(len(a)-1))/2
counts = Counter(a)

n_other_chars = 0
for c in counts.values():
    n_other_chars += (c * (c-1))/2

print(int(n_all_pairs - n_other_chars) + 1)


