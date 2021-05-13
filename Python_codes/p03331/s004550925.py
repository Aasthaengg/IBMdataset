from collections import Counter
 
n = input()
c = Counter(n)
c.pop('0', None)
 
if len(c) == 1 and '1' in c and c['1'] == 1:
    print(10)
else:
    print(sum(int(f) * m for f, m in c.items()))