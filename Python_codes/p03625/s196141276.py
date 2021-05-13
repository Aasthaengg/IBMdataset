from collections import Counter

n = int(input())
a = map(int, input().split())

c = Counter(a)
s = [(k, v) for k, v in c.items() if v >= 2]

s1 = s2 = 0  # s1 >= s2
for k, v in s:
    if k > s1:
        if v >= 4:
            s1 = s2 = k
        else:
            s1, s2 = k, s1
    elif k > s2:
        s2 = k

print(s1 * s2)
