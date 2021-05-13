from collections import Counter
s = Counter(input())
t = Counter(input())
s_n = sorted([x for x in s.values()])
t_n = sorted([x for x in t.values()])
print("Yes" if s_n==t_n else "No")