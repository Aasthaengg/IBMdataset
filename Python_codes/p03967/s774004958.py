import collections
s =input()
s2=collections.Counter(s)
gu = s2['g']
pa = s2['p']
point = len(s)//2-pa
print(point)