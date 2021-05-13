from collections import Counter
s = input()
n = len(s)
count = Counter()
for c in s:
    if c == 'p':
        count[0] += 1
    elif c == 'g':
        count[1] += 1
print(n//2-count[0])