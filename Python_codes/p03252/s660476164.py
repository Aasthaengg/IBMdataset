from collections import Counter
s1 = sorted(list(dict(Counter(input())).values()))
t1 = sorted(list(dict(Counter(input())).values()))
print(['No', 'Yes'][s1 == t1])