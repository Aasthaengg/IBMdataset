import collections
s = input()
c0 = s.count('0')
c1 = len(s) - c0
print(min(c0,c1)*2)